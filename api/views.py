from django.shortcuts import render
from django.http import HttpResponse

def simpfunc(request):
    return HttpResponse('Why did we call our App "api?"')

# Create your views here.
