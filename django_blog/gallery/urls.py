from django.urls import path

from . import views

app_name = 'gallery'

urlpatterns = [
    path('gallery/', views.gallery, name='gallery'),
    path('gallery/<slug:slug>/', views.AlbumDetail.as_view(), name='album'),
    # url(r'^(?P<slug>[-\w]+)$', app.views.AlbumDetail.as_view(), name='album'),
]
