# Generated by Django 3.0.8 on 2020-07-04 21:00

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(choices=[('Margherita', 'Margherita'), ('Salami', 'Salami'), ('Diavolo', 'Diavolo')], max_length=30)),
                ('size', models.CharField(choices=[('S', 'SMALL'), ('M', 'MEDIUM'), ('L', 'LARGE')], max_length=1)),
                ('slug', models.SlugField(unique=True)),
                ('image', models.ImageField(default='default.png', upload_to='pizza_img')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('pizza', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='pizzapp.Pizza')),
            ],
        ),
    ]
