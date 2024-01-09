from django.db import models

class Contact(models.Model):
    subject = models.CharField(max_length=200)
    message = models.CharField(max_length=500, default="message")
    sender = models.CharField(max_length=100)

def __str__(self):
        return self.sender