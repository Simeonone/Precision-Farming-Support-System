from django.db import models

# Create your models here.

class Customerpdf(models.Model):
    name = models.CharField(max_length=200)
    normal_image = models.ImageField()
    precision_map = models.ImageField()
    description = models.TextField()
    updated = models.DateField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)