from django.shortcuts import render

def info(request):
    return render(request, 'info.html')

def project(request):
    return render(request, 'project.html')
# Create your views here.
