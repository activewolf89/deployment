from django.shortcuts import render, redirect
from .models import Course
def index(request):
    b = Course.objects.all()
    print b
    context = {
    "courseRow": Course.objects.all()
    }
    return render(request, 'courseapp/index.html', context)

def posts(request):
    Course.objects.create(course_name = request.POST["course_name"], course_description = request.POST["course_description"])

    return redirect('/')

def remove(request, id):

    remove_context = {
    "course": Course.objects.get(id = id)
    }

    return render(request, 'courseapp/remove.html', remove_context)

def decision(request, id):
    instance = Course.objects.get(id=id)
    instance.delete()
    return redirect('/')

def resultreturn(request):
    return redirect('/')
