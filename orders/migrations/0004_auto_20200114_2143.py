# Generated by Django 3.0.2 on 2020-01-14 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_auto_20200114_2126'),
    ]

    operations = [
        migrations.CreateModel(
            name='SicilianPizzaType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=64)),
                ('priceSmall', models.FloatField()),
                ('priceLarge', models.FloatField()),
            ],
        ),
        migrations.RenameModel(
            old_name='Toppings',
            new_name='Topping',
        ),
    ]
