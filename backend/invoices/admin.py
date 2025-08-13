from django.contrib import admin
from .models import Invoice

@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('number', 'order', 'total', 'status', 'issued_at')
    search_fields = ('number', 'order__id', 'order__customer__username')
    list_filter = ('status', 'issued_at')