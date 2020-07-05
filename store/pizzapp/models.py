from django.db import models
from django.urls import reverse

from phonenumber_field.modelfields import PhoneNumberField
from PIL import Image


SIZES_CHOICES = (
    ('S', 'SMALL'),
    ('M', 'MEDIUM'),
    ('L', 'LARGE'),
)

TITLE_CHOICES = (
    ('Margherita', 'Margherita'),
    ('Salami', 'Salami'),
    ('Diavolo', 'Diavolo'),
)

class Pizza(models.Model):
    title       = models.CharField(max_length=30, choices=TITLE_CHOICES)
    size        = models.CharField(max_length=1, choices=SIZES_CHOICES)
    slug        = models.SlugField(unique=True)
    image       = models.ImageField(default='default.png', upload_to='pizza_img')

    def __str__(self):
        return f'{self.title}: {self.size}'

    def get_absolute_url(self):
        return reverse('menu-detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)


class Order(models.Model):
    name            = models.CharField(max_length=120)
    email           = models.EmailField()
    phone_number    = PhoneNumberField()
    pizza           = models.CharField(max_length=30)
    size            = models.CharField(max_length=1)

    def __str__(self):
        return f'{self.name}: {self.pizza} - {self.size}'
