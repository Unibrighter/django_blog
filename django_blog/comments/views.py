from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from blog.models import Post

from .models import Comment
from .forms import CommentForm


def post_comment(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            # return redirect(post)
        else:
            comment_list = post.comment_set.all()
            context = {'post': post,
                       'form': form,
                       'comment_list': comment_list
                       }
            return render(request, 'blog/single.html', context=context)
    return redirect(post)