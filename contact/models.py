from django.db import models
from django.contrib.auth.models import User

class Contact(models.Model):
    subject = models.CharField(max_length=200)
    message = models.CharField(max_length=500, default="message")
    sender = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, default ="email@email.com")

def __str__(self):
        return self.sender