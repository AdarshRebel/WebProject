from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    name= models.CharField(max_length=50)
    details = models.CharField(max_length=200)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url
