from django.shortcuts import render
from django.http import HttpResponse
from product.models import task  
def len2(text):
    return len(text)
def home(request):
    list_task = task.objects.all()
    titles = []
    for obj in list_task:
        length = len2(obj.tital)
        titles.append(str(obj.tital))
        new = ",".join(titles)
    return HttpResponse(new)


     