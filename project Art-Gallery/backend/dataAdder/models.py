# myapp/models.py

from django.db import models

class Image(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    price =models.IntegerField()
    category = models.CharField(max_length=100, default='null')
    
    def __str__(self):
        return self.title
