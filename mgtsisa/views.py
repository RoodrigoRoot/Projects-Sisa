from django.shortcuts import render, redirect
from django.views import View
from Profile.models import Profile

class IndexView(View):
    

    def get(self,request, *args, **kwargs):
        
        if request.user.is_authenticated:
            user = request.user.username
            auth = True if request.user.is_authenticated else False
            

        return render(request, 'index.html', locals())