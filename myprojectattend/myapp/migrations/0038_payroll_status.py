# Generated by Django 5.1.7 on 2025-04-01 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0037_rename_employeename_documentupload_employeename'),
    ]

    operations = [
        migrations.AddField(
            model_name='payroll',
            name='status',
            field=models.CharField(choices=[('Paid', 'Paid'), ('Pending', 'Pending')], default='Pending', max_length=20),
        ),
    ]
