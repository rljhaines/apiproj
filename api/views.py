from django.shortcuts import render
from django.http import HttpResponse

def simpfunc(request):
    return HttpResponse('Why did we call our App "api?"')

def anotherfunc(request):
    #print 'hello'
    return HttpResponse('<h2>Is HttpResponse required for a url view?</h2>')

#def anotherfunc(request):
    #print 'this is using a print function'

# Create your views here.
