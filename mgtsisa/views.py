from django.shortcuts import render, redirect
from django.views import View
from Profile.models import Profile
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect 
from django.template import RequestContext

class IndexView(View):
    

    def get(self,request, *args, **kwargs):
        
        if not request.user.is_authenticated:           
            return redirect('login')
            
            

        return render(request, 'index.html', locals() )

def logout_view(request):
    logout(request)
    return redirect('index')

    
def loginUser(request):  
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