# Generated by Django 5.1.7 on 2025-03-25 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0021_alter_employee_accountnumber_alter_employee_address_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='intime',
            field=models.TimeField(default='09:00:00', null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='outtime',
            field=models.TimeField(default='17:00:00', null=True),
        ),
    ]
