# Generated by Django 4.2.13 on 2025-03-11 11:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trainee', '0002_trainee_course_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='trainee',
            old_name='course_id',
            new_name='course',
        ),
    ]
