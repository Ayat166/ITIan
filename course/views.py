from django.shortcuts import render ,redirect

# Create your views here.
from .models import *


def courseList(request):
    courses=Course.objects.filter(status=True)
    return render(request,'courseList.html',{"courses":courses})


def addCourse(requset):
    if requset.method == "POST":
        courseName= requset.POST.get('name')
        Course.objects.create(name=courseName)
        return redirect('courseList')
    return render(requset,'courseForm.html')

def updateCourse(requset,id):
    course=Course.objects.get(id=id)
    if requset.method == "POST":
        courseName= requset.POST.get('name')
        courseEmail= requset.POST.get('email')
        course.name = courseName
        course.email = courseEmail
        course.save()
        return redirect('courseList')
    return render(requset,'updateCourse.html',{"course":course})

def deleteCourse(requset,id):
    course=Course.objects.get(id=id)   
    course.status=False
    course.save()
    return redirect('courseList')