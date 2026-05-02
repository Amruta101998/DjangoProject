# myapp/models.py
from django.db import models

class YourModel(models.Model):
    # Your model fields go here
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class YourMode(models.Model):
    # Your model fields go here
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name
