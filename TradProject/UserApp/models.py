from django.db import models
from django.utils import timezone
from django import forms

# Create your models here.

class Users(models.Model):
    username = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.username

class Post(models.Model):
    # user = models.CharField(max_length=100)
    text = models.TextField()
    created_at = models.DateTimeField(default=timezone.now())
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(Users, default=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.text

class ll(models.Model):
    pass