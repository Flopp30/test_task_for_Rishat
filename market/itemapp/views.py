import stripe
from django.conf import settings
from django.http import JsonResponse
from django.views import View
from django.views.generic import TemplateView
from .models import Item
stripe.api_key = settings.STRIPE_SECRET_KEY


class ItemLandingPageView(TemplateView):
    template_name = 'itemapp/landing.html'

    def get_context_data(self, **kwargs):
        item = Item.objects.get(name='Test item name')
        context = super(ItemLandingPageView, self).get_context_data(**kwargs)
        context.update({
            'item': item,
            'STRIPE_PUBLIC_KEY': settings.STRIPE_PUBLIC_KEY,
        })
        return context


class SuccessPageView(TemplateView):
    template_name = 'itemapp/success.html'


class CancelPageView(TemplateView):
    template_name = 'itemapp/cancel.html'


class CreateCheckoutSessionView(View):
    def post(self, request, *args, **kwargs):
        item_id = self.kwargs['pk']
        item = Item.objects.get(id=item_id)
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price_data': {
                        'currency': 'usd',
                        'unit_amount': item.price,
                        'product_data': {
                            'name': item.name
                        }
                    },
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url=settings.DOMAIN + '/item/success/',
            cancel_url=settings.DOMAIN + '/item/cancel/',
        )

        return JsonResponse({
            'id': checkout_session.id
        })
