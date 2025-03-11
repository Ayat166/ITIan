from django import forms

from course.models import Course
from trainee.models import Trainee

class CourseForm(forms.Form):
    name = forms.CharField(label="Name", max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))
    
class CourseUpdateForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name']  
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }