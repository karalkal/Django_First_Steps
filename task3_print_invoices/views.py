from django.shortcuts import render, HttpResponse
from django.shortcuts import render
from task3_print_invoices.models import Order


def display_receipt(request, order_number):
    try:
        found_order = Order.objects.get(id=order_number)
    except (Order.DoesNotExist):
        return HttpResponse("<h1>Nothing to display</h1><h2>In other words: <b>#### off!!!</b></h2>")

    context = {"found_order": found_order}

    return render(request, 'receipt.html', context)
