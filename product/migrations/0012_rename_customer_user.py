# Generated by Django 4.2.5 on 2023-09-26 07:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('admin', '0003_logentry_add_action_flag_choices'),
        ('product', '0011_delete_shippingaddress'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Customer',
            new_name='User',
        ),
    ]