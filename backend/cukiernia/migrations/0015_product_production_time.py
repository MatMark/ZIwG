# Generated by Django 3.1.8 on 2021-05-12 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cukiernia', '0014_auto_20210420_1202'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='production_time',
            field=models.IntegerField(default=3),
            preserve_default=False,
        ),
    ]
