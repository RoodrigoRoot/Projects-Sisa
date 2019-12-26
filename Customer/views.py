#Locals
from .forms import *
from .models import Customer

#Django
from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
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

class CreateCustomerView(View):

    def get(self, request, *args, **kwargs):
        form = CustomerRegisterForm()
        return render(request, 'create_customer.html', locals())

    def post(self, request, *args, **kwargs):
        form = CustomerRegisterForm(request.POST or None )
        if form.is_valid():
            name_bussines = request.POST['name_bussines']
            representative = request.POST['representative']
            phone = request.POST['phone']
            email = request.POST['email']
            customer = Customer.objects.create(name_bussines=name_bussines,email=email,phone=phone,representative=representative)
            customer.save()
            return redirect("customers")
        return render(request, 'create_customer.html', locals())

class EditCustomerView(View):

    @property
    def get_slug(self):
        return self.kwargs["slug"]
    
    
    def convertTuple(self, tup): 
        str =  ''.join(tup) 
        return str
    
    def get(self, request, *args, **kwargs):    
        
        customer = Customer.objects.get(slug=self.get_slug)
        forms = CustomerUpdateForm()
        return render(request, 'customer.html', locals())

    def post(self, request, *args, **kwargs):
        customer = False
        
        forms = CustomerUpdateForm(request.POST or None)
        
        if forms.is_valid():
            customer = Customer.objects.filter(slug=self.get_slug).update(
            representative = request.POST['representative'],
            phone = request.POST['phone'],
            email = request.POST['email']
            )
            return redirect('customers')
            
        
        return render(request, 'customer.html', locals())