# Generated by Django 4.0.2 on 2022-04-02 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0020_cart_user_id_alter_cart_description_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mpesa',
            name='Amount',
        ),
        migrations.RemoveField(
            model_name='notification',
            name='designer',
        ),
        migrations.AddField(
            model_name='mpesa',
            name='buyerid',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='mpesa',
            name='email',
            field=models.EmailField(default='sss@gmail.com', max_length=254),
        ),
        migrations.AddField(
            model_name='mpesa',
            name='pickupPoint',
            field=models.CharField(default='thika', max_length=200),
        ),
        migrations.AddField(
            model_name='mpesa',
            name='productid',
            field=models.ManyToManyField(to='mainapp.Mpesa'),
        ),
        migrations.AddField(
            model_name='notification',
            name='user_id',
            field=models.IntegerField(null=True),
        ),
    ]
