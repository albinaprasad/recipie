from django.db import models

# Create your models here.
class receipe(models.Model):
    rname=models.CharField(max_length=100)
    rdesc=models.TextField()
    rimage=models.ImageField(upload_to="recipe")