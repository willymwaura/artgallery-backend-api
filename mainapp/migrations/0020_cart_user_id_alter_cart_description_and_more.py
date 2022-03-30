# Generated by Django 4.0.2 on 2022-03-30 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0019_remove_cart_designer'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='user_id',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='cart',
            name='description',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='cart',
            name='designer_name',
            field=models.CharField(max_length=100),
        ),
    ]
