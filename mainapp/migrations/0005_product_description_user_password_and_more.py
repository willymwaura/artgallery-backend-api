# Generated by Django 4.0.2 on 2022-03-01 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_alter_user_phonenumber'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.CharField(default='lovely art', max_length=100),
        ),
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.IntegerField(default=1234),
        ),
        migrations.AlterField(
            model_name='cart',
            name='category',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='cart',
            name='designer',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='designer',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(max_length=10),
        ),
        migrations.DeleteModel(
            name='Artcategory',
        ),
        migrations.DeleteModel(
            name='Usercategory',
        ),
    ]
