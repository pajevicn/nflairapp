from django.db import models
from django.contrib.auth.models import User
from django.utils.datetime_safe import datetime


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.FileField()

    def delete(self, *args, **kwargs):
        # Najprije je potrebno pripremiti ono sto se zeli obrisati
        storage, path = self.image.storage, self.image.path
        # Brisanje modela pre fajla
        super(Profile, self).delete(*args, **kwargs)
        # brisanje fajla posle modela
        storage.delete(path)

    def __str__(self):
        return self.user

class Vijesti(models.Model):
    Naslov = models.CharField(max_length=32)
    Tekst = models.CharField(max_length=250)
    Slika = models.ImageField()

    def __str__(self):
        return self.Naslov

    class Meta:
        verbose_name_plural = "Vijesti"

class Blog(models.Model):
    Naslov = models.CharField(max_length=32)
    Tekst = models.CharField(max_length=250)
    Slika = models.ImageField()

    def __str__(self):
        return self.Naslov

    class Meta:
        verbose_name_plural = "Blog"

class Galerija(models.Model):
    Ime=models.CharField(max_length=32)
    Slika=models.ImageField()

    def __str__(self):
        return self.Ime
    class Meta:
        verbose_name_plural = "Galerija"

class Prodavnica(models.Model):
    Ime=models.CharField(max_length=32)
    Grad=models.CharField(max_length=32)
    Br_telefona=models.CharField(max_length=32)

    def __str__(self):
        return self.Ime

    class Meta:
        verbose_name_plural = "Prodavnica"

class Proizvod(models.Model):
    Ime=models.CharField(max_length=32)
    Stanje=models.IntegerField()
    Cijena=models.DecimalField(max_digits=1000, decimal_places=2)

    def __str__(self):
        return self.Ime

    class Meta:
        verbose_name_plural = "Proizvod"

class Prodaja(models.Model):
    VELICINA =(
        ('S','Male'),
        ('M', 'Srednje'),
        ('L', 'Velike'),
    )
    Broj_porudzbine=models.CharField(max_length=32)
    Proizvod = models.ManyToManyField(Proizvod)
    Cijena = models.DecimalField(max_digits=1000, decimal_places=2)
    Kolicina = models.DecimalField(max_digits=1000, decimal_places=2)
    Prodavnica=models.ForeignKey(User,on_delete=models.CASCADE)
    Datum_narucivanja=models.DateTimeField(default=datetime.now, blank=True)
    Ukupno=models.CharField(max_length=20, default='0')
    Velicina=models.CharField(max_length=4,null=True,choices=VELICINA)

    def racunanje(self):
        Ukupno=self.Cijena * self.Kolicina
        return Ukupno

    def save(self,*args,**kwargs):
        self.Ukupno=str(self.racunanje())
        super().save(*args,**kwargs)

    class Meta:
        verbose_name_plural = "Prodaja"

    def __str__(self):
        return self.Broj_porudzbine

class Porudzbina(models.Model):
    broj_p=models.CharField(max_length=32)
    prodavnica=models.ForeignKey(User,on_delete=models.CASCADE)
    model=models.ForeignKey(Proizvod,on_delete=models.CASCADE)
    zaduzeno=models.IntegerField()
    prodato=models.IntegerField()
    stanje=models.CharField(max_length=32, default='0')

    def racunaj(self):
        stanje=self.zaduzeno-self.prodato
        return stanje

    def save(self, *args,**kwargs):
        self.stanje=str(self.racunaj())
        super().save(*args,**kwargs)

    def __str__(self):
        return self.broj_p


