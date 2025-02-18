
from django.urls import path 
from . import views

urlpatterns = [
    path("",views.index, name="index"),
    path("about",views.about, name="about"),
    path("services",views.services, name="services"),
    path("services_details",views.services_details, name="services_details"),
    path("contact",views.contact, name="contact"),
    path("gallary",views.gallery, name="gallery"),
    
]


