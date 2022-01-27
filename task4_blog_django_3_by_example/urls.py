
from django.urls import path
from . import views

app_name = 'blog1'  # needed as we are using namespace in parent urls (I think...)
urlpatterns = [

    # post views
    path('', views.post_list, name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_detail, name='post_detail'),
]
