from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

# Create your models here.

class User(AbstractUser):
    pass

class Urlshort(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    url_asli = models.TextField()
    url_singkat = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100, null=True)
    waktu = models.DateTimeField(default=timezone.now)
    jumlah_klik = models.IntegerField(default=0)


class Analytics(models.Model):
    urlshort = models.ForeignKey(Urlshort, on_delete=models.CASCADE, null=True, blank=True)
    os_link = models.CharField(max_length=100)
    browser_link = models.CharField(max_length=100)
    device_link = models.CharField(max_length=100)
