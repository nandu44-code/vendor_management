from django.db import models
from django.db.models import Avg,Sum
import json

# Create your models here.
class Vendor(models.Model):
    name = models.TextField(max_length=50)
    contact_details = models.TextField(max_length=250)
    address = models.TextField(max_length=250)
    vendor_code = models.CharField(max_length=20,unique=True,primary_key=True)
    on_time_delivery_rate = models.FloatField(default=0)
    quality_rating_avg = models.FloatField(default=0)
    average_response_time = models.FloatField(default=0)
    fullfillment_rate = models.FloatField(default=0)

    def __str__(self):
        return self.name

class PurchaseOrder(models.Model):
    po_number = models.CharField(max_length=20, unique=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    order_date = models.DateTimeField()
    delivery_date = models.DateTimeField()
    delivered_date = models.DateTimeField(null=True, blank=True)
    items = models.JSONField()
    quantity = models.IntegerField()
    status = models.CharField(max_length=20)
    quality_rating = models.FloatField(null=True, blank=True)
    issue_date = models.DateTimeField()
    acknowledgment_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):  
        return self.po_number

class HistoricalPerformance(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    date = models.DateTimeField()
    on_time_delivery_rate = models.FloatField()
    quality_rating_avg = models.FloatField()
    average_response_time = models.FloatField()
    fulfillment_rate = models.FloatField()

    def __str__(self):
        return f"{self.vendor} - {self.date}"


class VendorPerformanceService:
    @staticmethod
    def update_on_time_delivery_rate(vendor):
        completed_orders = PurchaseOrder.objects.filter(vendor=vendor, status='completed')
        if completed_orders:
            on_time_deliveries = completed_orders.objects.filter(delivery_date__gte = F('delivered_date'))
            on_time_delivery_rate = on_time_deliveries.count()/completed_orders.count()
            vendor.on_time_delivery_rate = on_time_delivery_rate if on_time_delivery_rate else 0
            vendor.save()

    @staticmethod
    def update_quality_rating_avg(vendor):
        completed_orders_with_rating = PurchaseOrder.objects.filter(vendor=vendor, status='completed', quality_rating__isnull = False)
        quality_rating_avg =  completed_orders_with_rating.aggregate(Avg('quality_rating'))
        vendor.quliaty_rating_avg = quality_rating_avg
        vendor.save()

    @staticmethod
    def update_response_time_avg(vendor):
        response_times = PurchaseOrder.objects.filter(vendor=vendor, acknowledgment_date__isnull = False).values_list('acknowledgement_date', 'issue_date')
        if response_times:
            average_response_time = sum((acknowledgment_date - issue_date).total_secconds for acknowledgment_date , issue_date in response_times)/len(response_times)
        else:
            average_response_time = 0
        vendor.average_response_time = average_response_time
        vender.save()

    @staticmethod
    def update_fulfillment_rate(vendor):

        fulfilled_orders = PurchaseOrder.objects.filter(vendor=vendor , status='completed')
        total_orders = PurchaseOrder.objects.filter(vendor=vendor)
        fulfillment_rate = fulfilled_orders.count/total_orders.count
        ventor.fulfillment_rate = fulfillment_rate


