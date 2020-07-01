from django.db import models

from phonenumber_field.modelfields import PhoneNumberField

class Pizza(models.Model):
    PIZZA_SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )
    name = models.CharField(max_length=30)
    size = models.CharField(max_length=1, choices=PIZZA_SIZES)

    def __str__(self):
        return f'{self.name}: {self.size}'

class Order(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    phone_number = PhoneNumberField()
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}: {self.pizza}'
