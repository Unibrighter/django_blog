from django.shortcuts import render, get_object_or_404
from .models import Post
import markdown

# Create your views here.

def index(request):

    post_list = Post.objects.all().order_by('-created_time')

    return render(request=request,
                  template_name='blog/index.html',
                  context={
                      'title':'My new blog',
                      'welcome':'Welcome to my new blog!',
                      'post_list':post_list
                  })


def detail(request, post_id):
    post = get_object_or_404(Post, pk = post_id)
    post.body = markdown.markdown(post.body,
                                  extensions = [
                                      'markdown.extensions.extra',
                                      'markdown.extensions.codehilite',
                                      'markdown.extensions.toc',
                                  ])
    return render (request=request, template_name='blog/single.html', context= {'post':post})
