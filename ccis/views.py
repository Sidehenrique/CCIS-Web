from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def area(request):
   return render(request, 'ccis/area.html')


