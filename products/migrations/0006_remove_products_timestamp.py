# Generated by Django 4.0 on 2022-01-26 18:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_alter_products_is_available'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='timestamp',
        ),
    ]
