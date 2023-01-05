from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

@receiver(post_save, sender=User)
#we want a user profile to be created for each new user as opposed to
#creating directly from the admin panel
#the below function is run every time a user is created- the functionality is tied with the code
#above: @receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

#the following saves a user profile upon creation
@receiver(post_save,sender=User)
def save_profile(sender,instance,**kwargs):
    instance.profile.save()

#after creating this signals.py file:
#I imported the signals inside of the ready function of the users/apps.py file