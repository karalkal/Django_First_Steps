from django.contrib import admin
from django.urls import path

from task3_print_invoices import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.list_orders),
    path('<int:order_number>', views.display_receipt),
]
