from django import forms
from django.db.models import fields
from django.forms import widgets

from .models import Producto, Servicio

class ProductoForm(forms.ModelForm):

	class Meta:
		model = Producto

		fields = '__all__'

		widgets = {
			'nombre': forms.TextInput(attrs={'class': 'form-control'}),
		}

class ServicioForm(forms.ModelForm):

	class Meta:
		model = Servicio

		fields = '__all__'

		widgets = {
			'nombre': forms.TextInput(attrs={'class': 'form-control'})
		}