from django.db import models
from django.contrib.auth.models import AbstractUser
import datetime

# Create your models here.


# This is the information we got from sso
class User(AbstractUser):
    YEAR_CHOICES = []
    for r in range(2000, 3000):
        YEAR_CHOICES.append((r, r))

    name = models.CharField(
        max_length=100
    )

    npm = models.CharField(
        max_length=10,
        blank=True,
        null=True
    )

    generation = models.IntegerField(
        choices=YEAR_CHOICES,
        blank=True,
        null=True
    )

    faculty = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    study_program = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    educational_program = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )
