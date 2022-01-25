import datetime

from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def time_now(request):
    time_to_display = datetime.datetime.now()
    result_as_html = f"""
    <p>Local version of date: <b>{time_to_display.strftime('%x')}</b></p>
    <p>Local version of time: <b>{time_to_display.strftime('%X')}</b></p>
    <p>Weekday (full version): <b>{time_to_display.strftime('%A')}</b></p>
    <p>Local version of date and time: <b>{time_to_display.strftime('%c')}</b></p>
    """
    return HttpResponse(result_as_html)


def calculate_time(request, some_number):
    offset = int(some_number)
    amended_time = datetime.datetime.now() + datetime.timedelta(hours=offset)
    amended_date = datetime.datetime.now() + datetime.timedelta(days=offset)

    # ugly but it works - will add "s" if value > 1 or value < -1
    s = ""
    if offset > 1 or offset <-1:
        s = "s"

    if offset == 0:
        result_as_html = time_now("Хуй")

    elif offset > 0:
        result_as_html = f"""
        <p>In {offset} hour{s} it will be <b>{amended_time.strftime('%X')}</b></p>
        <p>In {offset} day{s} it will be <b>{amended_date.strftime('%x')}</b></p>
        """

    else:
        result_as_html = f""" 
        <p>{abs(offset)} hour{s} ago it was <b>{amended_time.strftime('%X')}</b></p>
        <p>{abs(offset)} day{s} ago it was  <b>{amended_date.strftime('%x')}</b></p>
        """

    return HttpResponse(result_as_html)
