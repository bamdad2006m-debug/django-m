from django.urls import path
from student.views import student_view,course_view
from student.class_views import AllStudentsView

app_name = "student"
urlpatterns = [
    path("all_students/",student_view, name="student_list"),
    path("courses/",course_view)
    # path("all_student_new", AllStudentsView.as_view())
]
