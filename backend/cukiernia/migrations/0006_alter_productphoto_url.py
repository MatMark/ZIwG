# Generated by Django 3.2 on 2021-04-12 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cukiernia', '0005_alter_carouselphoto_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productphoto',
            name='url',
            field=models.ImageField(upload_to='uploads/products/'),
        ),
    ]
