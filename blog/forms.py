from django import forms

from .models import Country, City, Street, Home


class CountryForm(forms.ModelForm):
    class Meta:
        model = Country
        fields = ['name']


class CityForm(forms.ModelForm):
    class Meta:
        model = City
        fields = ['city_name']


class StreetForm(forms.ModelForm):
    class Meta:
        model = Street
        fields = ['street_name']


class HomeForm(forms.ModelForm):
    class Meta:
        model = Home
        fields = ['home_name', 'description']




