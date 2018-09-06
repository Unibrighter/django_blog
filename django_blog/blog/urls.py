
from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('post/<int:post_id>/', views.detail, name = 'detail'),
    path('category/<int:category_id>', views.category, name = 'category'),
    path('archive/<int:year>/<int:month>', views.archive, name = 'archive'),
]
