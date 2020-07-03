from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.views.generic import ListView

from .forms import ContactForm
from .models import Pizza

def home(request):
    return render(request, 'pizzapp/home.html', {})

class PizzaView(ListView):
    model = Pizza
    context_object_name = 'pizzas'
    queryset = Pizza.objects.all()

def contact(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST or None)
        if form.is_valid():
            from_name = form.cleaned_data['name']
            from_email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            subject = 'Reservation'

            on_date = form.cleaned_data['date']
            on_time = form.cleaned_data['time']
            n_persons = form.cleaned_data['guests']
            message += f'\nam {on_date}, um {on_time} Uhr für {n_persons} Personen.\nAbgeschickt von {from_name}\n\n'
            try:
                send_mail(subject, message, from_email, ['admin@example.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, "pizzapp/contact.html", {'form': form})

def success(request):
    return render(request, "pizzapp/success.html")

