from django.db import models
from app_auth.models import User

# Create your models here.


# This is the additional information from user
class UserProfile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )
    photo = models.ImageField(
        blank=True,
        null=True
    )
    phone_number = models.CharField(
        max_length=20,
        blank=True,
        null=True
    )
    secondary_email = models.EmailField(
        max_length=100,
        blank=True,
        null=True
    )
    line_id = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )
    birth_date = models.DateField(
        blank=True,
        null=True
    )
    birth_place = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )
    home_address = models.CharField(
        max_length=500,
        blank=True,
        null=True
    )
    current_address = models.CharField(
        max_length=500,
        blank=True,
        null=True
    )

    def __str__(self):
        return self.user.name
