from django.shortcuts import render, get_object_or_404
from .models import Post, Category
from comments.forms import CommentForm
import markdown


# Create your views here.

def index(request):
    post_list = Post.objects.all()

    return render(request=request,
                  template_name='blog/index.html',
                  context={
                      'title': 'My new blog',
                      'welcome': 'Welcome to my new blog!',
                      'post_list': post_list
                  })


def archive(request, year, month):
    post_list = Post.objects.filter(
        created_time__year=year,
        created_time__month=month
    )

    return render(request=request,
                  template_name='blog/index.html',
                  context={
                      'post_list': post_list
                  })


def category(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    post_list = Post.objects.filter(category=category)
    return render(request, 'blog/index.html', context={'post_list': post_list})


def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post.body = markdown.markdown(post.body,
                                  extensions=[
                                      'markdown.extensions.extra',
                                      'markdown.extensions.codehilite',
                                      'markdown.extensions.toc',
                                  ])

    form = CommentForm()
    comment_list = post.comment_set.all()

    context = {
        'post': post,
        'form': form,
        'comment_list': comment_list
    }
    return render(request=request, template_name='blog/single.html', context=context)
