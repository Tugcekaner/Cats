from django.db import models

# ! python manage.py makemigrations
# ! python manage.py migrate 

# Create your models here.
class KediCins(models.Model):
    isim = models.CharField(max_length=100)
    aciklama = models.TextField()
    karakter = models.TextField()
    fiziksel = models.TextField()
    beslenme = models.TextField()
    egitim = models.TextField()
    saglik = models.TextField()
    resim = models.FileField(upload_to='urunler/',null=True)

    def __str__(self):
        return self.isim