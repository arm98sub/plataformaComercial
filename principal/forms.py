from django import forms
from django.db.models import fields
from django.forms import widgets, ModelForm, Textarea,ChoiceField

from .models import Producto, ProductoVendedor, Servicio

class ProductoForm(forms.ModelForm):

	class Meta:
		model = Producto

		fields = '__all__'

		widgets = {
			'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': Textarea(attrs={'cols': 20, 'rows': 5}),

		}
		
class ProductoFormVendedor(forms.ModelForm):
	class Meta:
		model = ProductoVendedor
		fields = '__all__'
		widgets = {
			'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': Textarea(attrs={'cols': 20, 'rows': 5}),

		}
		

class ServicioForm(forms.ModelForm):

	class Meta:
		model = Servicio

		fields = '__all__'

		widgets = {
			'nombre': forms.TextInput(attrs={'class': 'form-control'})
		}