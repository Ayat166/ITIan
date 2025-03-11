from django.shortcuts import render ,redirect

# Create your views here.
from .models import *
from .forms import *
def traineeList(request):
    trainees = Trainee.objects.filter(status=True)
    return render(request,'listtrainee.html',{"trainees":trainees})


def addTrainee(requset):
    context = {"form":ADDTraineeForm()}
    courses = Course.getAllCourses()
    context["courses"] = courses
    if requset.method == "POST":
        traineeName= requset.POST.get('name')
        traineeEmail= requset.POST.get('email')
        traineeCourse= Course.objects.get(id = requset.POST.get('course'))
        Trainee.objects.create(name=traineeName,email=traineeEmail,course=traineeCourse)
        return redirect('traineeList')
    return render(requset,'addTrainee.html',context)

def updateTrainee(requset,id):
    trainee=Trainee.objects.get(id=id)
    if requset.method == "POST":
        form = updateTraineeForm(requset.POST, instance=trainee)
        if form.is_valid():
            form.save()  
            return redirect('traineeList')
    else:
        form = updateTraineeForm(instance=trainee)  

    return render(requset,'updateTrainee.html',{"trainee":trainee,"form":form})

def deleteTrainee(requset,id):
    trainee=Trainee.objects.get(id=id)   
    trainee.status=False
    trainee.save()
    return redirect('traineeList')