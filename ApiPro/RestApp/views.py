from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import student
# Create your views here.


# def student(request):
#     students=[
#         {'id':1,'name':'sameer', 'age':24}
#     ]
#     return HttpResponse(students)

def StudentsView(request):
    students=student.objects.all()
    student_list=list(students.values())
    return JsonResponse(student_list,safe=False)