from django.contrib import admin
from .models import Prodavnica, Proizvod, Prodaja, Vijesti, Blog, Profile, Galerija,Porudzbina

# Register your models here.

admin.site.register(Prodavnica)
admin.site.register(Proizvod)
admin.site.register(Prodaja)
admin.site.register(Vijesti)
admin.site.register(Blog)
admin.site.register(Profile)
admin.site.register(Galerija)
admin.site.register(Porudzbina)