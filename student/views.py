from django.shortcuts import render

# def student_view(request):
#     all_student = student.objects.filter(score__gt=15)
#     context = {"students": all_student}
#     html_file = "student/all_student.html"
#     return render(request , html_file, context)
# def courses_view(request):
#     all_courses = course.objects.all()
#     context = {"courses": all_courses}
#     return render(request, "student/courses.html",context)

htmlfile = "student/all_student.html"
if request.method == "GET":
    all_students = student.objects.all()
    context = {"student": all_students , "form":form}
    return render(request , htmlfile,context)
elif request.method == "POST":
    data = request.POST
    fullname1 = data["fullname"]
    username1 = data["username"]
    phone1 = data["phone-number"]
    student.objects.create(fullname=fullname1,username=username1,phone=phone1,score=0)
    return render(request,htmlfile,{"form":form})