from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Advs
from .forms import AdvForm
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required

def index(request):
    advs = Advs.objects.all()
    context = {'advs' : advs}
    return render(request, 'advs/index.html', context)

def top_sellers(request):
    return render(request, 'advs/top-sellers.html')

@login_required(login_url=reverse_lazy('login'))
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
    return render(request, 'advs/advertisement-post.html', context)