# Generated by Django 4.2 on 2023-04-06 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0004_alter_student_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='marks',
            field=models.IntegerField(default=0),
        ),
    ]
