# Generated by Django 4.2 on 2023-04-06 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0002_rename_employees_student'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='emp_id',
        ),
        migrations.RemoveField(
            model_name='student',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='student',
            name='last_name',
        ),
        migrations.AddField(
            model_name='student',
            name='name',
            field=models.CharField(default='null', max_length=100),
        ),
    ]