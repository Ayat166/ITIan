from django import forms

from course.models import Course
from trainee.models import Trainee

class ADDTraineeForm(forms.Form):
    name = forms.CharField(label="Name", max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label="Email", widget=forms.EmailInput(attrs={'class': 'form-control'}))
    course = forms.ChoiceField(choices=[(course.id,course.name) for course in Course.getAllCourses()],
                                    label="Course",
                                    widget=forms.Select(attrs={'class': 'form-control'}))
    
    
class updateTraineeForm(forms.ModelForm):
    class Meta:
        model=Trainee
        fields = ['name','email','course']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'course': forms.Select(attrs={'class': 'form-control'}),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['course'].queryset = Course.getAllCourses()