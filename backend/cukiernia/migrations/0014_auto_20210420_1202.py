# Generated by Django 3.1.8 on 2021-04-20 12:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cukiernia', '0013_auto_20210420_1201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cukiernia.orderstatus'),
        ),
    ]
