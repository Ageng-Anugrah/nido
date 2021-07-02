from django.db import models
from app_auth.models import User

# Create your models here.


class BEM(models.Model):
    YEAR_CHOICES = []
    for r in range(2000, 3000):
        YEAR_CHOICES.append((r, r))

    name = models.CharField(
        max_length=255,
    )
    year = models.IntegerField(
        choices=YEAR_CHOICES
    )
    logo_url = models.CharField(
        max_length=500,
        blank=True,
        null=True
    )
    start_period = models.DateField()
    end_period = models.DateField()

    head = models.ForeignKey(
        User,
        blank=True,
        null=True,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name


class DepartmentScope(models.Model):
    name = models.CharField(
        max_length=100
    )

    chief = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name


class BEMDepartement(models.Model):
    name = models.CharField(
        max_length=100
    )
    description = models.CharField(
        max_length=500,
        blank=True,
    )
    head = models.OneToOneField(
        User,
        blank=True,
        null=True,
        on_delete=models.CASCADE
    )
    staff_amount = models.IntegerField(
        blank=True,
        null=True
    )
    bem = models.ForeignKey(
        BEM,
        on_delete=models.CASCADE,
        related_name='bem_departments'
    )
    scope = models.ForeignKey(
        DepartmentScope,
        on_delete=models.CASCADE,
        related_name='bem_departments',
        blank=True,
        null=True
    )

    def __str__(self):
        return str(self.name)


class BEMUser(models.Model):
    ROLE_CHOICES = [
        ('KETUA', 'KETUA'),
        ('DEPUTI', 'DEPUTI'),
        ('STAF_AHLI', 'STAF_AHLI'),
        ('STAF', 'STAF')
    ]

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )
    department = models.ForeignKey(
        BEMDepartement,
        on_delete=models.CASCADE,
        related_name='bem_users'
    )
    role = models.CharField(
        max_length=100,
        choices=ROLE_CHOICES
    )

    def __str__(self):
        return str(self.user.name)
