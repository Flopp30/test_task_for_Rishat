import stripe
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views import View
from django.views.generic import TemplateView

from .models import Item

stripe.api_key = settings.STRIPE_SECRET_KEY


class ItemsListPageView(TemplateView):
    template_name = 'itemapp/items_list.html'

    def get_context_data(self, **kwargs):
        items = Item.objects.filter(deleted=False)

        context = super(ItemsListPageView, self).get_context_data(**kwargs)
        context.update({
            'items': items,
        })
        return context


class ItemDetailPageView(TemplateView):
    template_name = 'itemapp/item_detail.html'

    def get_context_data(self, **kwargs):
        pk = self.kwargs.get('pk')
        item = get_object_or_404(Item, id=pk)

        context = super(ItemDetailPageView, self).get_context_data(**kwargs)
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
                            'name': item.name,
                            'images': [str(item.image)]
                        }
                    },
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url=settings.URL + '/success/',
            cancel_url=settings.URL + '/cancel/',
        )

        return JsonResponse({
            'id': checkout_session.id
        })


class StripeIntentView(View):
    def post(self, request, *args, **kwargs):
        try:
            item_id = self.kwargs['pk']
            item = Item.objects.get(id=item_id)
            intent = stripe.PaymentIntent.create(
                amount=item.price,
                currency='usd',
                automatic_payment_methods={
                    'enabled': True,
                },
            )
            return JsonResponse({
                'clientSecret': intent['client_secret']
            })
        except Exception as e:
            return JsonResponse({'error': str(e)})
