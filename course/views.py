from django.shortcuts import render ,redirect

# Create your views here.
from .models import *
from .forms import *

def courseList(request):
    courses=Course.objects.filter(status=True)
    return render(request,'courseList.html',{"courses":courses})


def addCourse(requset):
    context = {"form":CourseForm()}
    if requset.method == "POST":
        courseName= requset.POST.get('name')
        Course.objects.create(name=courseName)
        return redirect('courseList')
    return render(requset,'courseForm.html',context)

def updateCourse(requset,id):
    course=Course.objects.get(id=id)
    if requset.method == "POST":
        form = CourseUpdateForm(requset.POST, instance=course)
        if form.is_valid():
            form.save()  
            return redirect('courseList')
    else:
        form = CourseUpdateForm(instance=course)  
    return render(requset,'updateCourse.html',{"course":course,"form":form})

def deleteCourse(requset,id):
    course=Course.objects.get(id=id)   
    course.status=False
    course.save()
    return redirect('courseList')