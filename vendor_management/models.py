from django.db import models

# Create your models here.
class Vendor(models.Model):
    name = models.TextField(max_length=35)
    contact_details = models.TextField(max_length=100)
    address = models.TextField(max_length=100)
    vendor_code = models.CharField(max_length=20,unique=True)
    on_time_delivery_rate = models.FloatField()
    quality_rating_avg = models.FloatField()
    average_response_time = models.FloatField()
    fullfillment_rate = models.FloatField()
