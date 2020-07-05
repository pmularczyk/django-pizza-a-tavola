import django_filters

from .models import Order


class OrderFilter(django_filters.FilterSet):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.filters['name__icontains'].label = 'Name'
        self.filters['email__icontains'].label = 'Email'


    class Meta:
        model = Order
        fields = {
            'name': ['icontains'],
            'email': ['icontains'],
        }
