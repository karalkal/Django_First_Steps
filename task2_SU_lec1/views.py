from django.http import HttpResponse
from django.shortcuts import render
from task2_SU_lec1.models import Task


def index(request):
    tasks_list = Task.objects.all()
    # If objects in queryset, create dictionary with objects as values
    context = {'tasks_list': tasks_list}
    if not tasks_list:
        return HttpResponse("There are no created tasks!")

    return render(request, 'tasks/index.html', context)

