from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):    
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
