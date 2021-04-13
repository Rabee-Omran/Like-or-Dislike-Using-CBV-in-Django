from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Flower(models.Model):
    '''
    title
    image
    description
    '''
    title = models.CharField(max_length=100)
    title_ar = models.CharField(max_length=100)
    image = models.ImageField()
    description = models.TextField()
    description_ar = models.TextField()

    def __str__(self):
        return self.title





class Action(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    flower = models.ForeignKey(to=Flower, on_delete=models.CASCADE, related_name='actions')
    liked = models.BooleanField(null=True)

    class Meta:
        unique_together = ['user', 'flower']
