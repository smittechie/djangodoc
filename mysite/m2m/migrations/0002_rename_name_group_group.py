# Generated by Django 4.1.4 on 2023-01-23 10:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('m2m', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='group',
            old_name='name',
            new_name='group',
        ),
    ]
