# Generated by Django 4.2 on 2023-04-07 08:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0009_rename_subject_subject_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subject',
            old_name='name',
            new_name='subject',
        ),
    ]
