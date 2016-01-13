from django.shortcuts import render
from .models import Questions

# Create your views here.

def bereken(request):
    question=Questions.objects.all()
    return render(request, 'nrg/bereken.html', {'question':question})
