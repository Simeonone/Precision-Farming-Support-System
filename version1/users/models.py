from django.db import models
#i will be extending the user model that django provides
from django.contrib.auth.models import User
from PIL import Image

#class/model called profile that inherits from models.Model
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #cascade means that if the user is deleted, then also delete the profile
    #but if you delete the profile, it wont delete the user
    #-SIDENOTE - you can add other fields like bio or current city just as profile pic has been added as
    #shown below:
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    #default.jpg is the default image for any user
    #upload_to is the directory that images will be uploaded to when images will be uploaded
    #as shown below, a dunder str model is more specific compared to being more general(if it was, it would
    #display 'profile object'
    def __str__(self):
        return f'{self.user.username} Profile'
#the following code resizes a very large image
    #because large images can cause the website to run slow
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
#remember to review classes tutorial. Saved to list on google account
        img = Image.open(self.image.path)
        
        if img.height > 300 or img.width>300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)