from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import send_mail, BadHeaderError
from django.views.generic import DetailView, ListView, CreateView
from django.views.generic.edit import FormMixin

from .forms import ContactForm, OrderForm
from .models import Order, Pizza, Variation

def home(request):
    return render(request, 'pizzapp/home.html', {})


class PizzaView(ListView):
    model = Pizza
    context_object_name = 'pizzas'
    queryset = Pizza.objects.all()

class OrderListView(ListView):
    model = Order
    context_object_name = 'orders'
    queryset = Order.objects.all()


def order_pizza(request, slug):
    form = OrderForm()
    pizza = get_object_or_404(Pizza, slug=slug)
    template = 'pizzapp/pizza_detail.html'
    if request.method == 'POST':
        form = ContactForm(request.POST or None)
        print(form)
    return render(request, template, {'form': form})

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
    return render(request, 'pizzapp/contact.html', {'form': form})


def success(request):
    return render(request, 'pizzapp/success.html')

