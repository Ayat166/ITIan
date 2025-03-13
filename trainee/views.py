from django.shortcuts import render ,redirect
from django.views.generic import ListView ,DeleteView,UpdateView ,DetailView
from django.urls import reverse_lazy
from django.views import View

# Create your views here.
from .models import *
from .forms import *
def traineeList(request):
    trainees = Trainee.objects.filter(status=True)
    return render(request,'listtrainee.html',{"trainees":trainees})

class traineeListGeneric(ListView):
    model = Trainee
    fields='__all__'
    exclude = ['Status', ]
    template_name = 'listtrainee.html'
    queryset = Trainee.getAllTrainees()
    context_object_name = 'trainees'

class traineeListDeleteGeneric(UpdateView):
    model = Trainee
    fields = ["status"]
    success_url = reverse_lazy("traineeList")

    def get(self, request, *args, **kwargs):
        Trainee.deleteTraineeById(id=self.kwargs["pk"])
        return redirect(self.success_url)

class traineeListViewGeneric(DetailView):
    model = Trainee
    template_name = "traineeDetails.html"
    context_object_name = "trainee"
    

class traineeViewCreate(View):
    def get(self,request):
        context = {"form":ADDTraineeForm()}
        context["courses"] = Course.getAllCourses()
        return render(request,'addTrainee.html',context)
    def post(self,request):
        traineeName= request.POST.get('name')
        traineeEmail= request.POST.get('email')
        traineeCourse= Course.objects.get(id = request.POST.get('course'))
        Trainee.objects.create(name=traineeName,email=traineeEmail,course=traineeCourse)
        return redirect("traineeList")
    
class traineeViewUpdate(View):
    def get(self,request,id):
        trainee=Trainee.objects.get(id=id)
        context = {"form":updateTraineeForm(instance=trainee)}
        return render(request,'updateTrainee.html',context)
    def post(self,request,id):
        trainee=Trainee.objects.get(id=id)
        form = updateTraineeForm(request.POST, instance=trainee)
        if form.is_valid():
            form.save()  
            return redirect('traineeList')
        else:
            form = updateTraineeForm(instance=trainee)  
            return render(request,'updateTrainee.html',{"trainee":trainee,"form":form})




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