from django.db import models


class Book(models.Model):
    title = models.CharField(null=True, blank=True, max_length=50)
    author = models.CharField(null=True, blank=True, max_length=50)
    summary = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title

# Create your models here.
