from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField(max_length=5000)
    rating = models.FloatField(default=0)

    def __str__(self):
        return self.user.username
