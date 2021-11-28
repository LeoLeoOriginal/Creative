from django import forms
from django.forms import ModelForm
from .models import Order

class Order_form(ModelForm):
    class Meta():
        mode = Order
        fields = ('name','email','style','details')
        labels = {
            'name': 'Ingresa tu nombre completo',
            'email': 'Ingresa tu correo electrónico',
            'style': 'Elije tu estilo',
            'details':'Detalla tu pedido'
        }
        widgets = {
            'name': forms.TextInput(),
            'email': forms.EmailInput(),
            'style': forms.ChoiceField(),
            'details': forms.Textarea()
        }