from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from django.urls import reverse_lazy
from user.models import Profile
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
# Create your views here.


@method_decorator(login_required, name='dispatch')
class UserUpdateView(UpdateView):
    model = Profile
    template_name = 'update.html'
    context_object_name = 'user'
    fields = ('name', 'seller')

    def get_success_url(self):
        return reverse_lazy('user-detail', kwargs={'pk': self.object.id})


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'