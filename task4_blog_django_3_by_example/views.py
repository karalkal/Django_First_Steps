from django.shortcuts import render, HttpResponse

# Create your views here.
# def home(request):
#     return HttpResponse("Kur")

from django.shortcuts import render, get_object_or_404
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def post_list(request):
    object_list = Post.published.all()
    paginator = Paginator(object_list, 3)  # instance of Paginator class with 3 posts in each page
    page = request.GET.get('page')  # gets current page number
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)
    return render(request,
                  'blog1/post/list.html',
                  {'page': page,
                   'posts': posts})  # 'posts' key is linked to queryset of all Post objects


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post,  # get_objects of type Post with values slug=post, etc. (see params above)
                             slug=post,
                             status='published',
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)
    return render(request,
                  'blog1/post/detail.html',
                  {'post': post})
