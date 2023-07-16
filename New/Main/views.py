from django.shortcuts import render, Httpresponse

# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")