# Generated by Django 4.2 on 2023-04-07 08:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0011_alter_subject_student'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='student',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='subjects', to='newapp.student'),
        ),
    ]
