# Generated by Django 3.2.5 on 2022-06-17 05:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Member', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='last_login',
        ),
    ]
