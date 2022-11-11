from django.db import models


class Koylak(models.Model):
    mavsumi = models.CharField(max_length=20)
    uzunligi = models.CharField(max_length=20)
    olchami = models.IntegerField(default=1)
    def __str__(self):
        return f'siz bizning dokonimizdan {self.mavsumi} mavsumli koylakning {self.uzunligi} turidagisining {self.olchami} razmerini tanladingiz'

class Rubashka(models.Model):
    rangi = models.TextField()
    olchami = models.IntegerField(default=1)
    narxi = models.IntegerField(default=1)

    def __str__(self):
        return f'Siz bizning dokonimizdan {self.rangi} rangli rubashkamizdan {self.olchami} razmerdagisini {self.narxi} $ ga oldingiz'

class Kofta(models.Model):
    matosi = models.CharField(max_length=20)
    olchami = models.IntegerField(default=1)
    soni = models.IntegerField(default=1)

    def __str__(self):
        return f'Siz dokonimizdagi {self.matosi} matoli oq koftamizning {self.olchami} razmerlisidan {self.soni} dona oldingiz '

class Keta(models.Model):
    rangi = models.CharField(max_length=20)
    olchami = models.IntegerField(default=1)
    narxi = models.IntegerField(default=1)

    def __str__(self):
        return f'Siz {self.rangi} rangli  keta oyoq kiyimini {self.olchami} razmerlisini {self.narxi} $ ga xarid qildingiz' 

class Tufli(models.Model):
    matosi = models.TextField()
    turi = models.CharField(max_length=20)
    olchamini = models.IntegerField(default=1)

    def __str__(self):
        return f'Siz {self.matosi} matoli tuflini {self.turi}li turining {self.olchamini} razmerlisini tanladingiz'


class Palto(models.Model):
    matosi = models.CharField(max_length=20)
    uzunligi = models.TextField()
    olchami = models.IntegerField(default=1)

    def __str__(self):
        return f'Siz {self.matosi} matoli, {self.uzunligi} turli paltomizni  {self.olchami} razmerini tanladingiz'                

