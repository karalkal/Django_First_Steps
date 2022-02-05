from django.contrib import admin
from task3_print_invoices.models import Order


# admin.site.register(Order)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('person_name', 'product', 'company', 'ship_date', 'ordered_warranty')
