from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import SignUpForm

class CustomLoginView(LoginView):
    template_name = 'users/login.html'
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return reverse_lazy('core:index')

class CustomLogoutView(LogoutView):
    next_page = 'core:index'

class SignUpView(CreateView):
    form_class = SignUpForm
    template_name = 'users/signup.html'
    success_url = reverse_lazy('core:index')
    
    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        return response
    
    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if next_url:
            return next_url
        return super().get_success_url()