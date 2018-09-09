from django.urls import path

from . import views

app_name = 'comments'

urlpatterns = [
    path('comment/post/<int:post_id>', views.post_comment, name='post_comment'),
    # url('^comment/post/(?P<post_id>[0-9]+)/$', views.post_comment, name='post_comment'),
]
