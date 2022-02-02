from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from .models import Post
from .forms import EmailPostForm
from django.core.mail import send_mail
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# def post_list(request):
#     object_list = Post.published.all()
#     paginator = Paginator(object_list, 3)  # instance of Paginator class with 3 posts in each page
#     page = request.GET.get('page')  # gets current page number
#     try:
#         posts = paginator.page(page)
#     except PageNotAnInteger:
#         # If page is not an integer deliver the first page
#         posts = paginator.page(1)
#     except EmptyPage:
#         # If page is out of range deliver last page of results
#         posts = paginator.page(paginator.num_pages)
#     return render(request,
#                   'blog/post/list.html',
#                   {'page': page,
#                    'posts': posts})  # 'posts' key is linked to queryset of all Post objects

class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = "blog/post/list.html"


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


def post_share(request, post_id):
    # Retrieve post by id
    post = get_object_or_404(Post, id=post_id, status='published')
    sent = False

    if request.method == 'POST':  # if form has been submitted
        # create a form instance using the submitted data that is contained in request.POST
        form = EmailPostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data  # dictionary of form fields and their values
            # data ready to be emailed

            # retrieve the absolute path of the post using its get_absolute_url() method
            post_url = request.build_absolute_uri(post.get_absolute_url())

            subject = f"{cd['name']} recommends you read " \
                      f"{post.title}"
            message = f"Read {post.title} at {post_url}\n\n" \
                      f"{cd['name']}\'s comments: {cd['comments']}"

            send_mail(subject, message, 'admin@myblog.com',
                      [cd['to']])
            sent = True

    else:  # if method not POST, i.e. GET
        form = EmailPostForm()  # display blank form

    return render(request, 'blog/post/share.html', {'post': post,
                                                    'form': form,
                                                    'sent': sent})
