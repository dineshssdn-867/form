# Generated by Django 3.1.7 on 2021-03-05 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='email',
            field=models.EmailField(default=None, max_length=254, unique=True),
        ),
    ]
