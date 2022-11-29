from django.db import models

class Items(models.Model):
    is_active = models.BooleanField(default=False)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    slug = models.SlugField()
    price = models.FloatField(default=0)
    image = models.ImageField(upload_to="photos/")
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
