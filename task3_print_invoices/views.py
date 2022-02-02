from django.shortcuts import render, HttpResponse
from django.shortcuts import render
from django.views.generic import ListView

from task3_print_invoices.models import Order


def list_orders(request):
    all_orders = Order.objects.all()
    context = {"all_orders": all_orders}
    return render(request, 'orders_list.html', context)



def display_receipt(request, order_number):
    try:
        found_order = Order.objects.get(id=order_number)
    except (Order.DoesNotExist):
        return HttpResponse("<h1>Nothing to display</h1><h2>In other words: <b>#### off!!!</b></h2>")

    context = {"found_order": found_order}

    return render(request, 'receipt.html', context)
