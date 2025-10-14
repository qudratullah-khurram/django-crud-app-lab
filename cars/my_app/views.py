from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Car
from .models import Car, ServiceRecord


def home(request):
    return render(request, 'home.html')

class CarListView(ListView):
    model = Car
    template_name = 'car_list.html'
    context_object_name = 'cars'

class CarDetailView(DetailView):
    model = Car
    template_name = 'car_detail.html'

class CarCreateView(CreateView):
    model = Car
    template_name = 'car_form.html'
    fields = ['make', 'model', 'year', 'description']

class CarUpdateView(UpdateView):
    model = Car
    template_name = 'car_form.html'
    fields = ['make', 'model', 'year', 'description']

class CarDeleteView(DeleteView):
    model = Car
    template_name = 'car_confirm_delete.html'
    success_url = reverse_lazy('car_list')


class ServiceListView(ListView):
    model = ServiceRecord
    template_name = 'service_list.html'
    context_object_name = 'services'


class ServiceDetailView(DetailView):
    model = ServiceRecord
    template_name = 'service_detail.html'


class ServiceCreateView(CreateView):
    model = ServiceRecord
    fields = ['car', 'date', 'description', 'cost']
    template_name = 'service_form.html'


class ServiceUpdateView(UpdateView):
    model = ServiceRecord
    fields = ['car', 'date', 'description', 'cost']
    template_name = 'service_form.html'


class ServiceDeleteView(DeleteView):
    model = ServiceRecord
    template_name = 'service_confirm_delete.html'
    success_url = reverse_lazy('service_list')
