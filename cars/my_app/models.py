from django.db import models

# Create your models here.
from django.db import models
from django.urls import reverse

class Car(models.Model):
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.PositiveIntegerField()
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.make} {self.model} ({self.year})"

    def get_absolute_url(self):
        return reverse('car_detail', kwargs={'pk': self.pk})
