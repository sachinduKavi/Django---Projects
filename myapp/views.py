from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def firstFunction(request): 
    return render(request, 'template/index.js')