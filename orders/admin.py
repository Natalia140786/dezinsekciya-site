from django.contrib import admin
from .models import Order

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'service', 'created_at', 'is_processed')
    list_filter = ('is_processed', 'service')
    search_fields = ('name', 'phone')
