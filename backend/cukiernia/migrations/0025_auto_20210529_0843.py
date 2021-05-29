# Generated by Django 3.1.8 on 2021-05-29 08:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cukiernia', '0024_auto_20210527_1404'),
    ]

    operations = [
        migrations.RenameField(
            model_name='calendar',
            old_name='product_id',
            new_name='product',
        ),
        migrations.RenameField(
            model_name='combobox',
            old_name='product_id',
            new_name='product',
        ),
        migrations.RenameField(
            model_name='comboboxvalue',
            old_name='combo_box_id',
            new_name='combo_box',
        ),
        migrations.RenameField(
            model_name='decoration',
            old_name='order_id',
            new_name='order',
        ),
        migrations.RenameField(
            model_name='decoration',
            old_name='product_id',
            new_name='product',
        ),
        migrations.RenameField(
            model_name='instantretail',
            old_name='product_id',
            new_name='product',
        ),
        migrations.RenameField(
            model_name='ondemandretail',
            old_name='product_id',
            new_name='product',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='category_id',
            new_name='category',
        ),
        migrations.RenameField(
            model_name='productphoto',
            old_name='product_id',
            new_name='product',
        ),
        migrations.RenameField(
            model_name='textbox',
            old_name='product_id',
            new_name='product',
        ),
    ]
