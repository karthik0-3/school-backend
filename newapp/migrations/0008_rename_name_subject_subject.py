# Generated by Django 4.2 on 2023-04-07 08:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0007_subject_student_delete_subjectmark'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subject',
            old_name='name',
            new_name='subject',
        ),
    ]
