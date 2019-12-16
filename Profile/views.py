#Locals
from .forms import *
from .models import *
#Django
from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth import authenticate, login

class RegisterUserView(View):

    def get(self, request, *args, **kwargs):
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


def loginView(request):  
    if request.user.is_authenticated:
        return redirect('index')
        
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            #messages.success(request, "Bienvenido {}".format(username))
            return redirect('index')
        else:
            pass
            #messages.error(request, "Username or Password not valid")
    return render(request, 'login.html',locals())