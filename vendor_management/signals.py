from django.dispatch import receiver
from django.utils import timezone
from .models import PurchaseOrder, VendorPerformanceService

@receiver(post_save, sender = PurchaseOrder)
def update_vendor_performance(sender, instance, **kwargs):
    if instance.status == 'completed' and instance.delivered_date is None:
        instance.delivered_date = timezone.now()

    VendorPerformanceService.update_on_time_delivery_rate(instance.vendor)
    VendorPerformanceService.update_quality_rating_avgr(instance.vendor)
    VendorPerformanceService.update_response_time_avg(instance.vendor)
    VendorPerformanceService.fullfillment_rate(instance.vendor)
