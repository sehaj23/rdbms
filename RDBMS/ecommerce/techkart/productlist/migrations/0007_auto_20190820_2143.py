# Generated by Django 2.2.3 on 2019-08-20 16:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productlist', '0006_auto_20190820_2133'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productreviews',
            old_name='pid',
            new_name='product',
        ),
    ]
