# Generated by Django 5.1.7 on 2025-03-18 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='conformpassword',
            field=models.CharField(default=False, max_length=50),
        ),
        migrations.AddField(
            model_name='user',
            name='name',
            field=models.CharField(default=False, max_length=50),
        ),
    ]
