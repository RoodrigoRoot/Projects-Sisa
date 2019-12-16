from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('registro', RegisterUserView.as_view(), name="register" ),
    path('login', loginView, name="login" ),
]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
