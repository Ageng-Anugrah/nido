# Generated by Django 2.0.2 on 2019-05-13 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_profile', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
