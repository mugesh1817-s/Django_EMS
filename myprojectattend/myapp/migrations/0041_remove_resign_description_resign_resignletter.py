# Generated by Django 5.1.7 on 2025-04-01 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0040_resign_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resign',
            name='description',
        ),
        migrations.AddField(
            model_name='resign',
            name='resignletter',
            field=models.FileField(blank=True, null=True, upload_to='letters/'),
        ),
    ]
