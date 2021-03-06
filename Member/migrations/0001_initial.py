# Generated by Django 3.2.5 on 2022-06-23 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('email', models.EmailField(max_length=100, null=True)),
                ('username', models.CharField(max_length=20, unique=True)),
                ('phone', models.CharField(max_length=12)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'Member',
            },
        ),
    ]
