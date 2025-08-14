from django.db import models
from django.conf import settings
from django.core.validators import RegexValidator

# Validator لرقم الموبايل المصري
EG_PHONE_VALIDATOR = RegexValidator(
    regex=r'^(010|011|012|015)\d{8}$',
    message='Phone must be an Egyptian number like 010/011/012/015 + 8 digits.'
)

class Profile(models.Model):
    ROLE_CHOICES = (
        ('worker', 'Worker'),
        ('client', 'Client'),
        ('admin', 'Admin'),
    )

    # بدل User بـ settings.AUTH_USER_MODEL
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='profile'
    )
    phone = models.CharField(
        max_length=11,
        unique=True,
        validators=[EG_PHONE_VALIDATOR]
    )
    job_title = models.CharField(max_length=120, blank=True)
    role = models.CharField(
        max_length=10,
        choices=ROLE_CHOICES,
        default='client'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (self.user.get_full_name() or self.user.username) + f' ({self.role})'
