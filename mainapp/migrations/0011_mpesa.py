# Generated by Django 4.0.2 on 2022-03-08 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0010_delete_mpesa'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mpesa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PhoneNumber', models.IntegerField()),
                ('Amount', models.IntegerField()),
            ],
        ),
    ]
