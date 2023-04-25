from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse

# Create your views here.

def Student(request):
    SFO=StudentForm()
    d={'SFO':SFO}

    if request.method=='POST':
        SFOD=StudentForm(request.POST)
        
        if SFOD.is_valid():
            return HttpResponse(str(SFOD.cleaned_data))
        else:
            return HttpResponse("inserted is not validted")


    return render(request,'Student.html',d)