# Generated by Django 4.0 on 2024-12-01 15:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_alter_contact_email'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Contact',
        ),
    ]
