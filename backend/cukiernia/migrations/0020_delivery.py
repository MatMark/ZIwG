# Generated by Django 3.1.8 on 2021-05-12 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cukiernia', '0019_auto_20210512_1231'),
    ]

    operations = [
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_pl', models.CharField(max_length=25)),
                ('name_en', models.CharField(max_length=25)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
    ]
