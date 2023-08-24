from django.shortcuts import render
from django.http import HttpResponse
from .models import Advs

def index(request):
    advs = Advs.objects.all()
    context = {'advs' : advs}
    return render(request, 'index.html', context)

def top_sellers(request):
    return render(request, 'top-sellers.html')