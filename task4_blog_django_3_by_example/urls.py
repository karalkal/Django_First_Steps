from django.urls import path
from . import views

app_name = 'blog'  # needed as we are using namespace in parent urls (I think...)

urlpatterns = [
    path('', views.post_list, name='post_list'),
    # path('', views.PostListView.as_view(), name='post_list'),
    path('tag/<slug:tag_slug>/', views.post_list, name='post_list_by_tag'),
    # Both patterns point to the same view, but you are naming them
    # differently. The first pattern will call the post_list view without any optional
    # parameters, whereas the second pattern will call the view with the tag_slug parameter.

    path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_detail, name='post_detail'),
    path('<int:post_id>/share/', views.post_share, name='post_share'),
]
