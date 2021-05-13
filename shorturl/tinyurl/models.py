from django.db import models

class ShortUrl(models.Model):
    hash = models.CharField(max_length=32)
    url = models.TextField()
