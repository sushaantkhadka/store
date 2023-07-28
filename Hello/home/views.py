from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    return render(request, 'index.html')

def about(request):
    return HttpResponse("THis is a Aboutpage")

def services(request):
    return HttpResponse("THis is a servicespage")

def contact(request):
    return HttpResponse("THis is a contactpage")
