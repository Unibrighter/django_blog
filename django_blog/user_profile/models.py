from django.db import models

from django.contrib.auth.models import User

class Profile(models.Model):
    ## A nick name as the title of the profile page
    nickname = models.CharField(max_length = 64)

    ## A one-line status
    description = models.CharField(max_length = 140)

    ## A banner image to be displayed on the top of the profile page
    banner = models.ImageField(blank=True)

    ## A markdown document, including folding elements
    abstraction = models.TextField(blank=True)

    ## A resume to be download
    cv = models.FileField(blank=True)

    ## The user that links to the profile
    user = models.OneToOneField(User)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
