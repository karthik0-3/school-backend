from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .models import Student, Subject, SubjectMark
from .serializers import (
    StudentSerializer,
    SubjectSerializer,
    SubjectMarkSerializer,
    AverageMarkSerializer,
    MarkTableSerializer
)


# Create your views here.

def homeView(request):
    return render(request, "home.html", {})


class StudentList(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class SubjectList(ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class SubjectMarkList(ModelViewSet):
    queryset = SubjectMark.objects.all()
    serializer_class = SubjectMarkSerializer


class AvgList(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = AverageMarkSerializer


class MarkTable(ModelViewSet):
    queryset = SubjectMark.objects.all()
    serializer_class = MarkTableSerializer

    def list(self, request):
        output = []
        subjects = {}
        temp = {}
        single_student_data = {}

        for student in Student.objects.all():
            for subject in Subject.objects.all():
                t = SubjectMark.objects.filter(name=student, subject=subject)
                if t:
                    mark = t.values_list('mark', flat=True)[0]
                    id_ = t.values_list('id', flat=True)[0]
                    temp['mark'] = mark
                    temp['id'] = id_
                    subjects[subject.subject] = temp
                    temp = {}
                else:
                    temp['mark'] = None
                    subjects[subject.subject] = temp
                    temp = {}

            single_student_data[student.name] = subjects
            output.append(single_student_data)
            subjects = {}
            single_student_data = {}

        return Response(output)
