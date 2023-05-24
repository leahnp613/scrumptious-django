from django.db import models

# Create your models here.
class Recipe(models.Model):
    title = models.CharField(max_length =200)
    picture = models.URLField()
    description = models.TextField()
    created_on = models.DateTimeField(auto_now_add = True)
    author = models.CharField(max_length= 150, default= "User Name")

