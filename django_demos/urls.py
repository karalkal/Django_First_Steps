from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('time/', include('task1_datetime_demo.urls')),
    path('tasks/', include('task2_SU_lec1.urls')),
    path('receipts/', include('task3_print_invoices.urls')),
    path('blog/', include('task4_blog_django_3_by_example.urls', namespace='blog1')),
    # path('', task1_datetime_demo.views.time_now),
    # path('<str:some_number>/', task1_datetime_demo.views.calculate_time),
]
