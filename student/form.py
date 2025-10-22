from django.forms import ModelForm
from student.models import student

class StudentForm(ModelForm):
    
    class meta:
        model = student
        fields = ["fullname", "username","phone_number"]
        