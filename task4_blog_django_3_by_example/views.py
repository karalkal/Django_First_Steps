from django.shortcuts import render, HttpResponse

# Create your views here.
# def home(request):
#     return HttpResponse("Kur")

from django.shortcuts import render, get_object_or_404
from .models import Post


def post_list(request):
    posts = Post.published.all()
    return render(request,
                  'blog/post/list.html',
                  {'posts': posts})  # 'posts' key is linked to queryset of all Post objects


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post,  # get_objects of type Post with values slug=post, etc. (see params above)
                             slug=post,
                             status='published',
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)
    return render(request,
                  'blog/post/detail.html',
                  {'post': post})
