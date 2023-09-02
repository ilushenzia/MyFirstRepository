from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Advs
from .forms import AdvForm
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.db.models import Count

user = get_user_model()

def index(request):
    title = request.GET.get('query')
    if title:
        advs = Advs.objects.filter(title__icontains=title).order_by('-updated_at')
    else:
        advs = Advs.objects.all().order_by('-updated_at')
    context = {'advs' : advs,
               'title' : title,
               }
    return render(request, 'advs/index.html', context)

def top_sellers(request):
    sellers = user.objects.annotate(adv_count=Count('advs')).order_by('-adv_count')
    context = {'sellers': sellers}
    return render(request, 'advs/top-sellers.html', context)

@login_required(login_url=reverse_lazy('login'))
def adv_post(request):
    if request.method == 'POST':
        form = AdvForm(request.POST, request.FILES)
        if form.is_valid():
            # adv = Advs(**form.cleaned_data)
            adv = form.save(commit=False)
            adv.user = request.user
            adv.save()
            url = reverse('main')
            return redirect(url)
    else:
        form = AdvForm()
    context = {'form' : form}
    return render(request, 'advs/advertisement-post.html', context)

def adv_view(request, pk):
    adv = Advs.objects.get(id=pk)
    context = {'adv' : adv}
    return render(request, 'advs/advertisement.html', context)