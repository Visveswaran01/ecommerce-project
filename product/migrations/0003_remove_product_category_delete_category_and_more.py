# Generated by Django 4.2.5 on 2023-09-26 04:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='Category',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]