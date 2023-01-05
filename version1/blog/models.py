#remember to update admin.py, check html files e.g home.html, and views.py
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
#line 3 above; one to many relationship cause 1user=multiple posts,
#but multiple posts=1user == use of foreign key
from django.urls import reverse


#Post is a class, or model. and we are going to inherit from models.Model
#each class is going to be its own table in the database
class Post (models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    #(auto_now=True) - Update the date posted to the current date/time every time the post was updated
    #(auto_now_add=True) - sets the date posted to the current date/time only when the object is created. but
    #you cant ever update the value of the date posted
    #(default=timezone.now)-  changes the dates if you want to
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    #above line, if a user is deleted, then his posts too are deleted

    #below returns how we want e.g. a post to be printed out
    def __str__(self):
        return self.title
        #so, we return the title as written in above line, e.g in the database shell

#side note- here, we have post model and User(from admin url) model


#BELOW: within my post model, i neeed the getabsolute url method so that django knows how to find the location
#to a specific post. first, i am going to be getting the url for a specific route, using the reverse function,
#and not the redirect function, cause redirect redirects you to a specific route, but reverse will return the
#full url to the route as a string. in this case, i want to return the url as a string,a nd let the view
#handle the redirect for me.
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

