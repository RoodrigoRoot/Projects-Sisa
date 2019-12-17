from django.shortcuts import render
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import *
from .models import Customer
# Create your views here.

class AllCustomersView(LoginRequiredMixin, ListView):
    #querset = Customer.objects.all()
    login_url = '/login'
    #redirect_field_name = 'login'
    model = Customer
    template_name ="customer_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
