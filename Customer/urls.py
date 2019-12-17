from django.urls import path
from .views import *
urlpatterns = [
    path('', AllCustomersView.as_view(), name="customers")
]

