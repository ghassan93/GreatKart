# Generated by Django 3.1 on 2021-11-17 11:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0002_cartitem_variation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='variation',
        ),
    ]
