# Generated by Django 2.2.3 on 2019-08-23 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productlist', '0011_delete_cart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='p_specification',
            field=models.TextField(max_length=600),
        ),
    ]