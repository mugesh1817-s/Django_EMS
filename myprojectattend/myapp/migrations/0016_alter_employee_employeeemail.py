# Generated by Django 5.1.7 on 2025-03-24 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0015_employee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='employeeemail',
            field=models.CharField(max_length=50),
        ),
    ]
