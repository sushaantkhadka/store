from django.contrib import admin
from django.urls import path
from home import views

# To change the dashboard name of django admin 

admin.site.site_header = "Site Admin"
admin.site.site_title = "Site Admin Portal"
admin.site.index_title = "Welcome to Site Researcher Portal"

urlpatterns = [
    path("", views.index, name='home'),
    path("home", views.index, name='home'),
    path("about", views.about, name='about'),
    path("services", views.services, name='services'),
    path("contact", views.contact, name='contact'),
]