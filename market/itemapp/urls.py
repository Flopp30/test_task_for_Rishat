from django.urls import path
from itemapp.apps import ItemappConfig
from .views import (
    CreateCheckoutSessionView,
    ItemLandingPageView,
    SuccessPageView,
    CancelPageView,
)

app_name = ItemappConfig.name

urlpatterns = [
    path('create-checkout-session/<pk>/', CreateCheckoutSessionView.as_view(), name='create-checkout-session'),
    path('', ItemLandingPageView.as_view(), name='landing-page'),
    path('success/', SuccessPageView.as_view(), name='success-page'),
    path('cancel/', CancelPageView.as_view(), name='cancel-page'),
]
