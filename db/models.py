from django.db import models

# Sample User model
class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
