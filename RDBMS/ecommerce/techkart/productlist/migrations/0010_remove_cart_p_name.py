# Generated by Django 2.2.3 on 2019-08-20 20:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productlist', '0009_cart'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='p_name',
        ),
    ]
