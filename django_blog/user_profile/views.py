from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Profile

import markdown

# Create your views here.
def profile(request):
    # Default the user to the admin
    # TODO: change the email into variable loaded from env
    target_user = User.objects.filter(is_superuser=True, email = 'kunliang.wu@unibrighter.com')[0]

    profile = target_user.profile
    profile.abstraction = markdown.markdown(profile.abstraction,
                                  extensions=[
                                      'markdown.extensions.extra',
                                      'markdown.extensions.codehilite',
                                      'markdown.extensions.toc',
                                  ])

    context = {
        'profile': profile
    }
    return render(request=request, template_name='user_profile/profile.html', context=context)
