from django.shortcuts import redirect, render
from ndfapp.models import Service, Avis
from .forms import AvisForm, ContactForm


# Create your views here.

def home(request):
    services = Service.objects.all()
    avis_list = Avis.objects.all().order_by('-date')[:3]
    return render(request, 'ndf/home.html', {'services': services, 'avis_list': avis_list})

def avis(request):
    avis_list = Avis.objects.all().order_by('-date')
    if request.method == 'POST':
        form = AvisForm(request.POST)
        if form.is_valid():
            form.save()
            form = AvisForm()
            return redirect('avis')
    else:
        form = AvisForm()
        context = {
            'form': form,
            'avis_list': avis_list
        }
    return render(request, 'ndf/avis.html', context)

def contact(request):
    avis_list = Avis.objects.all().order_by('-date')[:3]
    success = False
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            success = True
            form = ContactForm()
            return redirect('home')
    else:
        form = ContactForm()
        context = {
            'form': form,
            'success': success,
            'avis_list': avis_list
        }
    return render(request, 'ndf/contact.html', context)


def about(request):
    avis_list = Avis.objects.all().order_by('-date')[:3] # [:3]passe les 3 derniers avis
    return render(request, 'ndf/about.html', {'avis_list': avis_list})
