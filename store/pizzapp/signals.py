from django.db.models.signals import pre_save
from django.utils.text import slugify

from .models import Pizza


def create_slug(instance, new_slug=None):
    slug = slugify(instance.name)
    if new_slug is not None:
        slug = new_slug

    queryset =  Pizza.objects.filter(slug=slug)
    if queryset.exists():
        new_slug = f'{slug}-{queryset.first().id}'
        return create_slug(instance, new_slug=new_slug)
    return slug

@receiver(pre_save, sender=Pizza)
def pre_save_pizza_reveiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)