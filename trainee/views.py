from django.shortcuts import render ,redirect

# Create your views here.
from .models import *

def traineeList(request):
    trainees = Trainee.objects.filter(status=True)
    return render(request,'listtrainee.html',{"trainees":trainees})


def addTrainee(requset):
    if requset.method == "POST":
        traineeName= requset.POST.get('name')
        traineeEmail= requset.POST.get('email')
        Trainee.objects.create(name=traineeName,email=traineeEmail)
        return redirect('traineeList')
    return render(requset,'addTrainee.html')

def updateTrainee(requset,id):
    trainee=Trainee.objects.get(id=id)
    if requset.method == "POST":
        traineeName= requset.POST.get('name')
        traineeEmail= requset.POST.get('email')
        trainee.name = traineeName
        trainee.email = traineeEmail
        trainee.save()
        return redirect('traineeList')
    return render(requset,'updateTrainee.html',{"trainee":trainee})

def deleteTrainee(requset,id):
    trainee=Trainee.objects.get(id=id)   
    trainee.status=False
    trainee.save()
    return redirect('traineeList')