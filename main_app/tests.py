from django.test import TestCase
from django.shortcuts import rennder
from .models import diseaseinfo 


def disease_views(request):


 if request.method == 'GET':
    #The list of diseases
    disease == diseaselist
    disease = request.GET.get('disease')

        if disease == "Malaria":
            return render(request, "malaria.html")