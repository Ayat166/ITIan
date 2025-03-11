from django.db import models

# Create your models here.

class Course(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, unique=True)
    status = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name 
    
    @classmethod
    def getAllCourses(cls):
        return cls.objects.filter(status=True)
    
    @classmethod
    def getCourseById(cls,id):
        return cls.objects.get(id=id)
        