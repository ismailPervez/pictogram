# Generated by Django 4.0.2 on 2022-02-06 03:46

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='date_posted',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
