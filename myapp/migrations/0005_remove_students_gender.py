# Generated by Django 4.0 on 2024-11-29 14:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_students_gender_alter_students_email_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='students',
            name='gender',
        ),
    ]
