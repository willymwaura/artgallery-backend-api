# Generated by Django 4.0.2 on 2022-03-02 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0006_remove_user_accesstoken_remove_user_refreshtoken'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='designer',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(max_length=100),
        ),
    ]
