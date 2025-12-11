# core/models.py
from django.db import models
from django.urls import reverse
from django.core.exceptions import ValidationError
from datetime import datetime, time as dtime

def clean(self):
    # verifica se já existe agendamento para a mesma cabeleireira, data e hora
    qs = Appointment.objects.filter(date=self.date, time=self.time)
    if self.stylist:
        qs = qs.filter(stylist=self.stylist)
    if self.pk:
        qs = qs.exclude(pk=self.pk)
    if qs.exists():
        raise ValidationError("Já existe um agendamento para este horário e profissional.")

class Service(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField(blank=True)
    duration_minutes = models.PositiveIntegerField(default=60)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"{self.name} - R${self.price}"

class Stylist(models.Model):
    name = models.CharField(max_length=120)
    bio = models.TextField(blank=True)
    photo = models.ImageField(upload_to='stylists/', blank=True, null=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Client(models.Model):
    name = models.CharField(max_length=120)
    phone = models.CharField(max_length=20)
    email = models.EmailField(blank=True)

    def __str__(self):
        return self.name

class Appointment(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.PROTECT)
    stylist = models.ForeignKey(Stylist, on_delete=models.SET_NULL, null=True, blank=True)
    date = models.DateField()
    time = models.TimeField()
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    confirmed = models.BooleanField(default=False)

    class Meta:
        ordering = ['date', 'time']

    def __str__(self):
        return f"{self.client} - {self.service} em {self.date} {self.time}"

    def get_absolute_url(self):
        return reverse('appointment_detail', args=[str(self.id)])

class GalleryImage(models.Model):
    title = models.CharField(max_length=120, blank=True)
    image = models.ImageField(upload_to='gallery/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title or f"Imagem {self.id}"
