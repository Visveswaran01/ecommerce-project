# Generated by Django 4.2.5 on 2023-09-26 07:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0012_rename_customer_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='user',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
