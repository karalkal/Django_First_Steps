"""django_demos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

import task1_datetime_demo.views
import task2_SU_lec1.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('time/', include('task1_datetime_demo.urls')),
    path('tasks/', include('task2_SU_lec1.urls')),
    path('receipts/', include('task3_print_invoices.urls')),
    path('blog1/', include('task4_blog_django_3_by_example.urls', namespace='blog1')),
    # path('', task1_datetime_demo.views.time_now),
    # path('<str:some_number>/', task1_datetime_demo.views.calculate_time),
]
