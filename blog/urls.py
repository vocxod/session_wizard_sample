from django.urls import path
from .views import AddressWizard


app_name = 'blog'


urlpatterns = [
    path('add-address/', AddressWizard.as_view(), name='add_address'),
]  
