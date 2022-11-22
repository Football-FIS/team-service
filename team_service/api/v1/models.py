from django.db import models
from django import forms

class Team(models.Model):
  user = models.CharField(max_length=150)
  password = forms.CharField(widget=forms.PasswordInput)
  email = models.EmailField(max_length=254)
  latitude = models.DecimalField(max_digits=9, decimal_places=6)
  longuitude = models.DecimalField(max_digits=9, decimal_places=6)
  expiration = models.DateField() 
  planType = models.TextField()


  class Meta:
    ordering = ['user']
