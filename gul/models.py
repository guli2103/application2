from django.db import models

class Atirgul(models.Model):
    rangi = models.CharField(max_length=20)
    soni = models.CharField(max_length=20)
    narxi = models.IntegerField(default=1)

    def __str__(self):
        return f'Siz {self.rangi} rangli atirguldan {self.soni} donasini {self.narxi} $ ga oldingiz'

class Lola(models.Model):
    qayerdanligi = models.CharField(max_length=20)
    rangi = models.CharField(max_length=20)
    soni = models.IntegerField(default=1)

    def __str__(self):
        return f'Siz {self.qayerdanligi} lolasining {self.rangi} rangidan {self.soni} dona oldingiz'

class Binafsha(models.Model):
    nomi = models.CharField(max_length=20)
    soni = models.IntegerField(default=1)
    narxi = models.IntegerField(default=1)

    def __str__(self):
        return f'Siz bizning {self.nomi} gulimizdan, {self.soni} donasini va {self.narxi} $ga xarid qildingiz'

class Liliya(models.Model):
    rangi = models.CharField(max_length=20)
    soni = models.IntegerField(default=1)
    narxi = models.IntegerField(default=1)

    def __str__(self):
        return f'Siz bizning {self.rangi} rangli liliya gulimizdan {self.soni} donasini {self.narxi} $ ga xarid qildingiz'


class Moychechak(models.Model):
    kattaligi =  models.TextField()
    soni = models.IntegerField(default=1)
    narxi = models.IntegerField(default=1)

    def __str__(self):
        return f'Siz moychechak gulimizning {self.kattaligi} hajmlisidan {self.soni} donasini {self.narxi} $ ga oldingiz'

class Arxediya(models.Model):
    rangi = models.TextField()
    soni = models.IntegerField(default=1)
    narxi = models.IntegerField(default=1)

    def __str__(self):
        return f'Siz bizning gullar do\'konimizdan {self.rangi} rangli arxediya gulidan {self.soni} donasini {self.narxi} $ ga xarid qildingiz  '