# Generated by Django 3.1.8 on 2021-04-19 10:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_currentuser.db.models.fields
import django_currentuser.middleware


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cukiernia', '0011_textbox_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_date', models.DateField()),
                ('delivery_date', models.DateField()),
                ('status_pl', models.CharField(choices=[('zlozone', 'Złożone'), ('oplacone', 'Opłacone'), ('zrealizowane', 'Zrealizowane')], max_length=50)),
                ('status_en', models.CharField(choices=[('ordered', 'Ordered'), ('paid', 'Paid'), ('complete', 'Complete')], max_length=50)),
                ('street', models.CharField(blank=True, default='', max_length=100)),
                ('postcode', models.CharField(blank=True, default='', max_length=6)),
                ('city', models.CharField(blank=True, default='', max_length=50)),
                ('courier_note', models.TextField(max_length=500)),
                ('dealer_note', models.TextField(max_length=500)),
                ('delivery', models.CharField(choices=[('odbior', 'Odbiór osobisty'), ('kurier', 'Kurier')], max_length=50)),
                ('price', models.FloatField()),
                ('products', models.ManyToManyField(to='cukiernia.Product')),
                ('user', django_currentuser.db.models.fields.CurrentUserField(default=django_currentuser.middleware.get_current_authenticated_user, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
