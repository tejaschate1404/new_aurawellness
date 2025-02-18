from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'client/index.html')

def about(request):
    return render(request, 'client/about.html')


def services(request):
    return render(request, 'client/services.html')


def services_details(request):
    return render(request, 'client/services_details.html')


def contact(request):
    return render(request, 'client/contact.html')


def gallery(request):
    return render(request, 'client/gallery.html')