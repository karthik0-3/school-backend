from django.db import models


# from django.db.models import Avg


class Student(models.Model):
    name = models.CharField(default='', max_length=100)  # null=false, blank=false

    def __str__(self):
        return self.name


class Subject(models.Model):
    # student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='subjects', default='')
    subject = models.CharField(default='', max_length=25)  # subject=>name, null=false, blank=false, unique=true

    def __str__(self):
        return self.subject


class SubjectMark(models.Model):  # model name should be Mark
    name = models.ForeignKey(Student, on_delete=models.CASCADE)  # name=>student
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='subjects')
    mark = models.FloatField()  # min=0.00 - 100.00
