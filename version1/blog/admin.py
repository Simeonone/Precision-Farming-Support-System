from django.contrib import admin
#use here to show data in admin path of your website
#we are going to register our models here in order to show in the admin page
from .models import Post
admin.site.register(Post)
