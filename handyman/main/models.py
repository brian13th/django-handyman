from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=200)
    context = models.CharField(max_length=500)
    author = models.ForeignKey(User , on_delete=models.CASCADE)

    def __str__(self):
        return self.title
