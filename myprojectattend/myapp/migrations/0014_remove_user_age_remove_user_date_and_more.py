# Generated by Django 5.1.7 on 2025-03-22 07:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0013_user_employeeemail_alter_user_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='age',
        ),
        migrations.RemoveField(
            model_name='user',
            name='date',
        ),
        migrations.RemoveField(
            model_name='user',
            name='department',
        ),
        migrations.RemoveField(
            model_name='user',
            name='education',
        ),
        migrations.RemoveField(
            model_name='user',
            name='employeeemail',
        ),
        migrations.RemoveField(
            model_name='user',
            name='employeeid',
        ),
        migrations.RemoveField(
            model_name='user',
            name='employeename',
        ),
        migrations.RemoveField(
            model_name='user',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='user',
            name='lastname',
        ),
        migrations.RemoveField(
            model_name='user',
            name='mobile',
        ),
        migrations.RemoveField(
            model_name='user',
            name='picture',
        ),
        migrations.RemoveField(
            model_name='user',
            name='salary',
        ),
    ]
