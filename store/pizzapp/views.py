from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.mail import BadHeaderError
from django.views.generic import ListView

from .filters import OrderFilter
from .forms import OrderForm
from .models import Order, Pizza

class PizzaView(ListView):
    model = Pizza
    context_object_name = 'pizzas'
    queryset = Pizza.objects.all()

class OrderListView(ListView):
    model = Order
    context_object_name = 'orders'
    queryset = Order.objects.all()
    # paginate_by = 12

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = OrderFilter(self.request.GET, queryset=self.get_queryset())
        return context


def home(request):
    return render(request, 'pizzapp/home.html', {})

def success(request):
    return render(request, 'pizzapp/success.html')

def impressum(request):
    return render(request, 'pizzapp/impressum.html')

def detail(request, slug):
    pizza = Pizza.objects.get(slug=slug)
    initital = {'pizza': pizza.title,'size': pizza.size}
    form = OrderForm(initial=initital)
    if request.method == 'POST':
        form = OrderForm(request.POST or None, initial=initital)
        if form.is_valid():
            try:
                form.save()
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, 'pizzapp/pizza_detail.html', {'form': form})
