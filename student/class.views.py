from django.views import View
from student.models import *
from student.form import StudentForm
from django.shortcuts import render,redirect

class  AllStudentsView(View):
    html_file = "student/all_student.html"
    
    def get(self,request):
        form = StudentForm()
        all_student = Student.objects.all()
        context = {"student":
            all_student,"form":form}
        return render(request,self.html_file,context)