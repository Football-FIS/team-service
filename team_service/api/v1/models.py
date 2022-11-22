from djongo import models
from django.utils.crypto import get_random_string


class Team(models.Model):
  id = models.CharField(primary_key=True, max_length=24, default=get_random_string(length=24))
  user = models.CharField(max_length=150)
  password = models.CharField(max_length=150)
  email = models.EmailField(max_length=254)
  latitude = models.DecimalField(max_digits=9, decimal_places=6)
  longuitude = models.DecimalField(max_digits=9, decimal_places=6)
  expiration = models.DateField() 
  planType = models.TextField()

  class Meta:
    ordering = ['user']
