from django.contrib import admin
#below i am importing the users Profile(for profile pic) model that i just created
from .models import Profile

admin.site.register(Profile)
#after adding this, try rerunning the server
