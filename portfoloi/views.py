from django.shortcuts import render
from gallery.models import Gallery


def home(response):
    gallerys = Gallery.objects
    return render(response, 'home.html', {'gallery': gallerys})
