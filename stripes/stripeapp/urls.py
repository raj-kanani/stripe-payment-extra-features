from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.conf import settings
from django.conf.urls.static import static
from . import views


router = DefaultRouter()
router.register('product', views.ProductView, basename='product')

urlpatterns = [

    path('a/', include(router.urls)),
    path('auth', include('rest_framework.urls', namespace='rest_framework')),

    path('create-payment-intent/<pk>/', views.StripeIntentView.as_view(), name='create-payment-intent'),
    path('webhooks/stripe/', views.stripe_webhook, name='stripe-webhook'),
    path('cancel/', views.CancelView.as_view(), name='cancel'),
    path('success/', views.SuccessView.as_view(), name='success'),
    path('', views.ProductLandingPageView.as_view(), name='landing-page'),
    path('create-checkout-session/<pk>/', views.CreateCheckoutSessionView.as_view(), name='create-checkout-session')
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
