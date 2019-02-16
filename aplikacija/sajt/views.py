from django.http import HttpResponse, request
from django.shortcuts import render
from django.template import loader
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView
from django.views import generic, View

from .models import Prodaja,Proizvod,Prodavnica,Vijesti


class index(generic.ListView):
    template_name = 'index.html'
    context_object_name = 'categories'

    def get_queryset(self):
        return Vijesti.objects.all()[:10]

class narudzbina(generic.ListView):
    template_name = 'narudzbina.html'
    context_object_name = 'narucivanje'


    def get_queryset(self):
       return Prodaja.object.all()

class prodza(generic.ListView):
    template_name = 'prodavnica.html'
    context_object_name = 'prodza'

    def get_queryset(self):
        return Prodavnica.objects.all()

class proizvodi(generic.ListView):
    template_name = 'proizvodi.html'
    context_object_name = 'proizvodi'

    def get_queryset(self):
        return Proizvod.objects.all()

class NovaProdavnica(CreateView):
    template_name = 'kreiranjeProdavnica.html'
    model = Prodavnica

    fields = ['Ime', 'Grad','Br_telefona']
    success_url = reverse_lazy('aplikacija:prodza')

class NoviProizvod(CreateView):
    template_name = 'kreiranjeProizvoda.html'
    model = Proizvod

    fields = ['Ime', 'Stanje', 'Cijena']
    success_url = reverse_lazy('aplikacija:proizvodi')
class NovaPorudzbina(CreateView):
    template_name = 'kreiranjeporudzbine.html'
    model = Prodaja

    fields = ['Broj_porudzbine','Proizvod','Cijena','Kolicina','Prodavnica','Datum_narucivanja','Ukupno','Velicina']
    success_url = reverse_lazy('aplikacija:prodza')

class administratorView(generic.ListView):
    template_name = 'administracija.html'
    context_object_name = 'entries'

    def get_queryset(self):
        return Prodavnica.objects.all()

def search(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        proj = Proizvod.objects.filter(Ime__icontains=q)
        return render(request, 'pretraga.html', {'proj': proj, 'query': q})
    else:
        return HttpResponse('Please submit a search term.')
class detailView(generic.DetailView):
    template_name = 'proizvodi.html'
    model = Proizvod

    def get_context_data(self, **kwargs):

        context = super(detailView, self).get_context_data(**kwargs)
        context["all_roles"] = Proizvod.objects.all()
        return context
