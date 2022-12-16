from djongo import models
from django.contrib.auth.models import User
# from django.utils.crypto import get_random_string


class Team(models.Model):
    PLAN_TYPE = [
        ('FRE', 'Free'),
        ('PRE', 'Premium'),
        ('ENT', 'Enterprise')
    ]

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    name = models.CharField(max_length=255, null=True)
    country = models.CharField(max_length=255, null=True)
    state = models.CharField(max_length=255, null=True)
    address = models.CharField(max_length=255, null=True)
    coach_name = models.CharField(max_length=255, null=True)
    stadium_name = models.CharField(max_length=255, null=True)
    president_name = models.CharField(max_length=255, null=True)
    league_name = models.CharField(max_length=255, null=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True)
    longuitude = models.DecimalField(max_digits=9, decimal_places=6, null=True)
    expiration = models.DateField(null=True)
    plan_type = models.CharField(
        max_length=3,
        choices=PLAN_TYPE,
        default='FRE',
    )

    class Meta:
        ordering = ['user']
