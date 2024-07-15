from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView
from student.models import Student
from teacher.models import Teacher
from period.models import Period
from course.models import Course
from classRoom.models import Room
from api.serializers import PeriodSerializer, CourseSerializer, ClassSerializer, StudentSerializer, TeacherSerializer
from .serializers import  StudentSerializer

class StudentListView(APIView):
    def get(self,  request):
        Students = Student.objects.all()
        serializer = StudentSerializer(Students, many=True)
        return Response(serializer.data)
    
class TeacherListViews(APIView):
    def get(self, request):
        teacher = Teacher.objects.all()
        serializer = TeacherSerializer(teacher, many=True)
        return Response(serializer.data)
    
class CourseListViews(APIView):
    def get(self, request):
        course = Course.objects.all()
        serializer = CourseSerializer(course, many=True)
        return Response(serializer.data)
    
class classRoomListViews(APIView):
    def get(self, request):
        Room = Room.objects.all()
        serializer = ClassSerializer(Room, many=True)
        return Response(serializer.data)
    
class PeriodListViews(APIView):
    def get(self, request):
        period = Period.objects.all()
        serializer = PeriodSerializer(period, many=True)
        return Response(serializer.data)