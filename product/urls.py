from django.urls import path
from product.views import home
 
urlpatterns = [
     path("home/", home)
     path("task_student/<int:st_id>/",task_student)
]

 