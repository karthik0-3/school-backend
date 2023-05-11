# Generated by Django 4.2 on 2023-04-06 16:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0005_student_marks'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=25)),
            ],
        ),
        migrations.RemoveField(
            model_name='student',
            name='marks',
        ),
        migrations.CreateModel(
            name='SubjectMark',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mark', models.FloatField()),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='newapp.student')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='newapp.subject')),
            ],
        ),
    ]
