from django.db import models
from django.utils import timezone

class Invoice(models.Model):
    UNPAID = 'unpaid'
    PAID = 'paid'
    VOID = 'void'
    STATUS_CHOICES = [
        (UNPAID, 'Unpaid'),
        (PAID, 'Paid'),
        (VOID, 'Void'),
    ]

    order = models.OneToOneField('orders.Order', on_delete=models.CASCADE, related_name='invoice')

    number = models.CharField(max_length=32, unique=True, editable=False)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    tax = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    currency = models.CharField(max_length=8, default='EGP')

    issued_at = models.DateTimeField(auto_now_add=True)
    due_at = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=UNPAID)
    notes = models.TextField(blank=True)

    def save(self, *args, **kwargs):
        creating = self.pk is None
        super().save(*args, **kwargs)

        if creating and not self.number:
            self.number = f"INV-{timezone.now():%Y%m%d}-{self.pk:06d}"
            super().save(update_fields=['number'])

    def __str__(self):
        return self.number
