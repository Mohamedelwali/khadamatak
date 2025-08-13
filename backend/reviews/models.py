from django.db import models
from django.utils import timezone
from services.models import Service


class Review(models.Model):
    """User review for a service."""
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name="reviews")
    reviewer_name = models.CharField(max_length=120)
    rating = models.IntegerField()  # 1 to 5
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.service.title} - {self.rating}★ by {self.reviewer_name}"
