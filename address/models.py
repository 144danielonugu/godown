from django.db import models

# Create your models here.
class Address(models.Model):
    fellowship=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    time=models.DateTimeField(auto_now_add=True)
    body=models.TextField()
    slug=models.SlugField
