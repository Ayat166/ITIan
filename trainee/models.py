from django.db import models

from course.models import Course

# Create your models here.
class Trainee(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255,null=False)
    email = models.EmailField(unique=True,null=False)
    status = models.BooleanField(default=True)
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    
    
    @classmethod
    def getAllTrainees(cls):
        return cls.objects.filter(status=True)
    
    @classmethod
    def getTraineeById(cls,id):
        return cls.objects.get(id=id)
        