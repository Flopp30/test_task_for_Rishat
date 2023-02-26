from django.urls import path
from apps import ItemappConfig
from .views import (
    CreateCheckoutSessionView,
    StripeIntentView,
    ItemsListPageView,
    ItemDetailPageView,
    SuccessPageView,
    CancelPageView,
)

app_name = ItemappConfig.name

urlpatterns = [
    path('buy/<int:pk>/', CreateCheckoutSessionView.as_view(), name='create-checkout-session'),
    path('create-payment-intent/<int:pk>/', StripeIntentView.as_view(), name='create-payment-intent'),
    path('', ItemsListPageView.as_view(), name='items-list-page'),
    path('item/<int:pk>', ItemDetailPageView.as_view(), name='item-detail-page'),
    path('success/', SuccessPageView.as_view(), name='success-page'),
    path('cancel/', CancelPageView.as_view(), name='cancel-page'),
]
