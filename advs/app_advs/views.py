from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Advs
from .forms import AdvForm
from django.urls import reverse

def index(request):
    advs = Advs.objects.all()
    context = {'advs' : advs}
    return render(request, 'index.html', context)

def top_sellers(request):
    return render(request, 'top-sellers.html')

def adv_post(request):
    if request.method == 'POST':
        form = AdvForm(request.POST, request.FILES)
        if form.is_valid():
            # adv = Advs(**form.cleaned_data)
            adv = form.save(commit = False)
            adv.user = request.user
            adv.save()
            url = reverse('main')
            return redirect(url)
    else:
        form = AdvForm()
    context = {'form' : form}
    return render(request, 'advertisement-post.html', context)