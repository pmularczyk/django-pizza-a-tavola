from django.db import models
from django.urls import reverse

from phonenumber_field.modelfields import PhoneNumberField
from PIL import Image


class Pizza(models.Model):
    name        = models.CharField(max_length=30)
    slug        = models.SlugField(unique=True)
    description = models.TextField(max_length=240, default="Pizza description")
    image       = models.ImageField(default='default.png', upload_to='pizza_img')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('menu-detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)


class VariationManager(models.Manager):
    def all(self):
        return super().filter(active=True)

    def sizes(self):
        return self.all().filter(category='size')


VARIATION_CATEGORIES = (
    ('size', 'size'),
)

SIZES_CHOICES = (
    ('S', 'SMALL'),
    ('M', 'MEDIUM'),
    ('L', 'LARGE'),
)

class Variation(models.Model):
    pizza       = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    category    = models.CharField(
        max_length=20,
        choices=VARIATION_CATEGORIES,
        default='size'
    )
    title       = models.CharField(max_length=20, choices=SIZES_CHOICES)
    active      = models.BooleanField(default=True)

    objects     = VariationManager()

    def __str__(self):
        return f'{self.pizza}: {self.title}'


class Order(models.Model):
    name            = models.CharField(max_length=120)
    email           = models.EmailField()
    phone_number    = PhoneNumberField()
    variation       = models.ForeignKey(Variation, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}: {self.variation}'
