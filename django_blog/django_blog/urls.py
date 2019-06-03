"""django_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

# TODO: need to 1. figure out the reason why we need to add the static setting urls
# TODO: 2. set up the nginx proxy server
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # This will take a while for the sniffers to find
    path('Commandos1984/', admin.site.urls),
    path('', include('blog.urls')),
    path('', include('comments.urls')),
    path('', include('user_profile.urls')),
    path('', include('gallery.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)