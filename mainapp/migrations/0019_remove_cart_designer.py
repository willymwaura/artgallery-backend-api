# Generated by Django 4.0.2 on 2022-03-30 07:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0018_cart_description_cart_designer_id_cart_designer_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='designer',
        ),
    ]
