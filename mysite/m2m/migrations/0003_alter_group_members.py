# Generated by Django 4.1.4 on 2023-01-23 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('m2m', '0002_rename_name_group_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='members',
            field=models.ManyToManyField(related_name='members', through='m2m.Membership', to='m2m.person'),
        ),
    ]
