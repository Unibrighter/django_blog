from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='detail'),
    path('category/<int:pk>', views.CategoryView.as_view(), name='category'),
    path('archive/<int:year>/<int:month>', views.ArchiveView.as_view(), name='archive'),
]
