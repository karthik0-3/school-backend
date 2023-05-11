from rest_framework import serializers
from .models import Student, Subject, SubjectMark
from django.db.models import Avg, Sum


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['id', 'subject']


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name']


class SubjectMarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubjectMark
        fields = ['id', 'name', 'subject', 'mark']


class AverageMarkSerializer(serializers.ModelSerializer):
    average_marks = serializers.SerializerMethodField(read_only=True)
    total_marks = serializers.SerializerMethodField(read_only=True)
    count_avg = 0
    count_sum = 0

    class Meta:
        model = SubjectMark

        fields = ["name", "average_marks", "total_marks"]

    def get_average_marks(self, object):
        i = self.count_avg

        while i < len(Student.objects.all()):
            self.count_avg += 1
            temp = SubjectMark.objects.filter(name=Student.objects.all()[i]).aggregate(Avg('mark')).values()
            for i in temp:
                return float(format(i, '.2f'))

    def get_total_marks(self, object):
        i = self.count_sum

        while i < len(Student.objects.all()):
            self.count_sum += 1
            temp = SubjectMark.objects.filter(name=Student.objects.all()[i]).aggregate(Sum('mark')).values()
            for i in temp:
                return float(format(i, '.2f'))


class MarkTableSerializer(serializers.ModelSerializer):

    class Meta:
        model = SubjectMark
        fields = SubjectSerializer.Meta.fields


