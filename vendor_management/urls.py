from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import VendorViewset, PurchaseOrderViewset

router = DefaultRouter()

router.register('vendors', VendorViewset)
router.register('purchase_orders', PurchaseOrderViewset)

urlpatterns = [
    path('',include(router.urls))
]
