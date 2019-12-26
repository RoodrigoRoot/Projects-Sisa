from django.urls import path
from .views import *
urlpatterns = [
    path('', AllCustomersView.as_view(), name="customers"),
    path('crear/', CreateCustomerView.as_view(), name="create_customers"),
    path('editar/<slug:slug>/', EditCustomerView.as_view(), name="edit_customers")
]

