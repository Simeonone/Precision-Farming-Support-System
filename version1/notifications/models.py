from django.db import models

# Create your models here.

class Notifications(models.Model):
    message = models.TextField()
    image = models.ImageField(upload_to='adminrequests/')

    def __str__(self):
        return self.message
