# Generated by Django 4.2.13 on 2025-03-09 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]
