# Generated by Django 4.2.3 on 2023-07-31 12:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bake_cake_bot', '0011_alter_order_init_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='init_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 31, 12, 37, 34, 215508, tzinfo=datetime.timezone.utc), verbose_name='Дата создания заказа'),
        ),
    ]
