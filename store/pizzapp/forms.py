from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100)
    email = forms.EmailField(label='Email')
    phone = forms.IntegerField(required=False)
    date = forms.DateField(label='Datum', widget=forms.TextInput(attrs={'type': 'date'}))
    time = forms.TimeField(label='Uhrzeit', widget=forms.TextInput(attrs={'type': 'time'}))
    guests = forms.IntegerField(label='Personenanzahl',min_value=1, max_value=100)
    message = forms.CharField(label='Ihre Nachricht', widget=forms.Textarea, required=False)