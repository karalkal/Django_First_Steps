# Generated by Django 4.0.1 on 2022-01-23 01:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task3_print_invoices', '0002_order_delete_orders'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='ordered_warranty',
            field=models.BooleanField(default=False),
        ),
    ]
