from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def homepage(request):
    return render(request, 'firstapplication/welcome.html')
    # constraint 01
    # return HttpResponse("Welcome to my first django web app")   