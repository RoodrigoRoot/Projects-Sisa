#Locals
from .forms import *
from .models import *
#Django
from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth import authenticate, login, logout

class RegisterUserView(View):

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('index')
        form1 = ProfileRegisterForm()
        form2 = UserRegisterForm()

        return render(request, 'register.html', locals())
    
    def post(self, request, *args, **kwargs):
        form1 = ProfileRegisterForm(request.POST)
        form2 = UserRegisterForm(request.POST)
        
        if form1.is_valid() and form2.is_valid():
            user = form2.save()
            area = request.POST.get('area')
            profile = Profile.objects.create(user=user,area=area)
            profile.save()

        return render(request, 'register.html', locals())

