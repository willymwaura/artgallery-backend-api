# Generated by Django 4.0.2 on 2022-04-03 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0022_remove_mpesa_productid_mpesa_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='product_id',
            field=models.IntegerField(default=1),
        ),
    ]
