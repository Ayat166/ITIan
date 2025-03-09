from django.db import models

# Create your models here.
class Trainee(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255,null=False)
    email = models.EmailField(unique=True,null=False)
    status = models.BooleanField(default=True)