from django.db import models

# Create your models here.
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Car(models.Model):
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.PositiveIntegerField()
    description = models.TextField(blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.make} {self.model} ({self.year})"

    def get_absolute_url(self):
        return reverse('car_detail', kwargs={'pk': self.pk})

class ServiceRecord(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='services')
    date = models.DateField()
    description = models.TextField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Service on {self.date} - ${self.cost}"

    def get_absolute_url(self):
        return reverse('service_detail', kwargs={'pk': self.pk})