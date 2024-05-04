from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import VendorViewset, PurchaseOrderViewset

router = DefaultRouter()

router.register('vendors', VendorViewset, basename='vendor')
router.register('purchase_orders', PurchaseOrderViewset, basename='purchase_order')

urlpatterns = [
    path('',include(router.urls))
]
