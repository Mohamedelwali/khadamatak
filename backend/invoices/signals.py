from django.db.models.signals import post_save
from django.dispatch import receiver
from decimal import Decimal
from orders.models import Order
from .models import Invoice

COMPLETED_STATUS = 'completed'  

@receiver(post_save, sender=Order)
def create_invoice_when_completed(sender, instance, created, **kwargs):

    if getattr(instance, 'status', None) != COMPLETED_STATUS:
        return


    if hasattr(instance, 'invoice'):
        return


    service = getattr(instance, 'service', None)
    subtotal = Decimal(service.price) if service and service.price is not None else Decimal('0.00')
    tax = Decimal('0.00')  
    total = subtotal + tax

    Invoice.objects.create(
        order=instance,
        subtotal=subtotal,
        tax=tax,
        total=total,
        currency='EGP',
        status=Invoice.UNPAID,
    )
