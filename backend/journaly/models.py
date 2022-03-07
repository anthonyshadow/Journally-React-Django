import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    password = models.CharField(max_length=200)
    age = models.IntegerField()
    location = models.CharField(max_length=200)
    bio = models.CharField(max_length=250)
    avatar = models.ImageField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name, self.last_name, self.email, self.bio, self.location, self.password

class Calendar(models.Model):
    date = models.DateTimeField(auto_now_add=True)


class Journal(models.Model):
    journal_title = models.CharField(max_length=200)
    mood_rating = models.IntegerField()
    text = models.TextField()
    image= models.ImageField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.journal_title, self.text

class Exercise(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    exercise_name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    image_url = models.ImageField()
    source_url = models.URLField()

    def __str__(self):
        return self.exercise_name, self.description


