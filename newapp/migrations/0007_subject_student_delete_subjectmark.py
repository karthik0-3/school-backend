# Generated by Django 4.2 on 2023-04-07 07:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0006_subject_remove_student_marks_subjectmark'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='student',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='newapp.student'),
        ),
        migrations.DeleteModel(
            name='SubjectMark',
        ),
    ]