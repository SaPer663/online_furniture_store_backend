# Generated by Django 4.2.2 on 2023-06-20 20:06

import apps.orders.validators
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [('product', '0001_initial'), migrations.swappable_dependency(settings.AUTH_USER_MODEL)]

    operations = [
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=200, verbose_name='Адрес')),
                (
                    'phone',
                    models.CharField(
                        max_length=30, validators=[apps.orders.validators.validate_phone], verbose_name='Телефон'
                    ),
                ),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата оформления')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
            ],
            options={'verbose_name': 'Доставка', 'verbose_name_plural': 'Доставка'},
        ),
        migrations.CreateModel(
            name='DeliveryType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True)),
            ],
            options={'verbose_name': 'Способ доставки', 'verbose_name_plural': 'Способы  доставки'},
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата заказа')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Дата обновления заказа')),
                ('paid', models.BooleanField(default=False, verbose_name='Оплачено')),
                ('total_cost', models.DecimalField(decimal_places=2, max_digits=40, verbose_name='Общая стоимость')),
                (
                    'delivery',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name='order_delivery',
                        to='orders.delivery',
                        verbose_name='Доставка',
                    ),
                ),
            ],
            options={'verbose_name': 'Заказ', 'verbose_name_plural': 'Заказы', 'ordering': ('-created',)},
        ),
        migrations.CreateModel(
            name='Storehouse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                (
                    'quantity',
                    models.PositiveIntegerField(
                        validators=[
                            django.core.validators.MinValueValidator(
                                limit_value=0, message='Минимальное количество 0!'
                            )
                        ]
                    ),
                ),
                (
                    'product',
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='storehouse',
                        to='product.product',
                        verbose_name='Товар',
                    ),
                ),
            ],
            options={'verbose_name': 'Склад', 'verbose_name_plural': 'Склад'},
        ),
        migrations.CreateModel(
            name='OrderProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1, verbose_name='Колличество')),
                ('price', models.DecimalField(decimal_places=2, max_digits=20, verbose_name='Цена')),
                ('cost', models.DecimalField(decimal_places=2, max_digits=40, verbose_name='Стоимость')),
                (
                    'order',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='items',
                        to='orders.order',
                        verbose_name='Заказ',
                    ),
                ),
                (
                    'product',
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name='order_item',
                        to='product.product',
                        verbose_name='Товар',
                    ),
                ),
            ],
            options={'verbose_name': 'Товар в заказе', 'verbose_name_plural': 'Товары в заказе'},
        ),
        migrations.AddField(
            model_name='order',
            name='products',
            field=models.ManyToManyField(through='orders.OrderProduct', to='product.product', verbose_name='Товар'),
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name='orders',
                to=settings.AUTH_USER_MODEL,
                verbose_name='Клиент',
            ),
        ),
        migrations.AddField(
            model_name='delivery',
            name='type_delivery',
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name='delivery',
                to='orders.deliverytype',
                verbose_name='Доставка',
            ),
        ),
        migrations.AddField(
            model_name='delivery',
            name='user',
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name='delivery',
                to=settings.AUTH_USER_MODEL,
                verbose_name='Клиент',
            ),
        ),
    ]
