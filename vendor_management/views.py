from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import VendorSerializer, PurchaseOrderSerializer

# Create your views here.
class VendorViewset(viewsets.ModelViewSet):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

class PurchaseOrderViewset(viewsets.ModelViewSet):
    queryset = Vendor.objects.all()
    serializer_class = PurchaseOrderSerializer
