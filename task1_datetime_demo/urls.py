from django.urls import path
from . import views

app_name = 'time'  # needed as we are using namespace in parent urls (I think...)


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.time_now),
    path('<str:some_number>/', views.calculate_time),
]
