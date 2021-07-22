from django.db import models

# Create your models here.

class Text(models.Model):
    name = models.CharField(max_length=300)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name