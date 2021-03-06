# Generated by Django 3.1.8 on 2021-04-20 12:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cukiernia', '0012_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_pl', models.CharField(max_length=25)),
                ('name_en', models.CharField(max_length=25)),
            ],
        ),
        migrations.RemoveField(
            model_name='order',
            name='status_en',
        ),
        migrations.RemoveField(
            model_name='order',
            name='status_pl',
        ),
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='cukiernia.orderstatus'),
        ),
    ]
