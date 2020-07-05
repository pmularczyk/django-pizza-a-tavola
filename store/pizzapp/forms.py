from django import forms
from .models import Order

class OrderForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
       super().__init__(*args, **kwargs)
       self.fields['pizza'].widget.attrs['readonly'] = True
       self.fields['size'].widget.attrs['readonly'] = True

    class Meta:
        model   = Order
        fields  = ('name', 'email', 'phone_number', 'pizza', 'size')
