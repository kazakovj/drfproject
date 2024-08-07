from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    owner = models.ForeignKey(User, related_name='products', on_delete=models.CASCADE)

    def __str__(self):
        return self.name