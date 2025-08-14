from django.db import models
from django.utils import timezone

class ServiceCategory(models.Model):
    """Type of service (e.g., Plumbing, Carpentry)."""
    name = models.CharField(max_length=120, unique=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


class Service(models.Model):
    """A service offered by a provider."""
    provider_name = models.CharField(max_length=255, default='Unknown Provider')
    category = models.ForeignKey(
        ServiceCategory, on_delete=models.SET_NULL, null=True, related_name="services"
    )
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    city = models.CharField(max_length=120, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.title} — {self.provider_name}"
