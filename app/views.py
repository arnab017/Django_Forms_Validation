from django.shortcuts import render
from app.models import *
from app.forms import *
from django.http import HttpResponse
# Create your views here.

def sf(request):
    SFO = StudentForm()
    d = {'SFO': SFO}
    if request.method == 'POST':
        SFD = StudentForm(request.POST)
        if SFD.is_valid():
            return HttpResponse('VALID DATA')
        else:
            return HttpResponse('INVALID DATA')
    return render(request,'sf.html',d)