from django.shortcuts import render, redirect

# Create your views here.
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Car
from .models import Car, ServiceRecord
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin




class Home(LoginView):
    template_name = 'home.html'

class CarListView(LoginRequiredMixin, ListView):
    model = Car
    template_name = 'car_list.html'
    context_object_name = 'cars'

    def get_queryset(self):
        return Car.objects.filter(user=self.request.user)

class CarDetailView(LoginRequiredMixin, DetailView):
    model = Car
    template_name = 'car_detail.html'

class CarCreateView(LoginRequiredMixin, CreateView):
    model = Car
    template_name = 'car_form.html'
    fields = ['make', 'model', 'year', 'description']
    def form_valid(self, form):
        form.instance.user = self.request.user 
        return super().form_valid(form)

class CarUpdateView(LoginRequiredMixin, UpdateView):
    model = Car
    template_name = 'car_form.html'
    fields = ['make', 'model', 'year', 'description']

class CarDeleteView(LoginRequiredMixin, DeleteView):
    model = Car
    template_name = 'car_confirm_delete.html'
    success_url = reverse_lazy('car_list')


class ServiceListView(LoginRequiredMixin, ListView):
    model = ServiceRecord
    template_name = 'service_list.html'
    context_object_name = 'services'


class ServiceDetailView(LoginRequiredMixin, DetailView):
    model = ServiceRecord
    template_name = 'service_detail.html'


class ServiceCreateView(LoginRequiredMixin, CreateView):
    model = ServiceRecord
    fields = ['car', 'date', 'description', 'cost']
    template_name = 'service_form.html'


class ServiceUpdateView(LoginRequiredMixin, UpdateView):
    model = ServiceRecord
    fields = ['car', 'date', 'description', 'cost']
    template_name = 'service_form.html'


class ServiceDeleteView(LoginRequiredMixin, DeleteView):
    model = ServiceRecord
    template_name = 'service_confirm_delete.html'
    success_url = reverse_lazy('service_list')


def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('car_list')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)
