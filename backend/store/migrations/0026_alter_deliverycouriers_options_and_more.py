# Generated by Django 4.2 on 2024-01-03 21:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0025_alter_product_description'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='deliverycouriers',
            options={'ordering': ['name'], 'verbose_name_plural': 'Delivery Couriers'},
        ),
        migrations.RenameField(
            model_name='deliverycouriers',
            old_name='couriers_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='deliverycouriers',
            old_name='couriers_tracking_website_address',
            new_name='tracking_website',
        ),
        migrations.RemoveField(
            model_name='deliverycouriers',
            name='date',
        ),
        migrations.RemoveField(
            model_name='deliverycouriers',
            name='url_parameter',
        ),
    ]
