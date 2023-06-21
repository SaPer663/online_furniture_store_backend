# Generated by Django 4.2.2 on 2023-06-21 13:09

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [('product', '0005_collection_alter_product_description_and_more')]

    operations = [
        migrations.AlterField(
            model_name='discount',
            name='discount_created_at',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Начало скидки'),
        ),
        migrations.AlterField(
            model_name='discount', name='discount_end_at', field=models.DateField(verbose_name='Окончание скидки')
        ),
        migrations.AlterField(
            model_name='product',
            name='material',
            field=models.ManyToManyField(related_name='products', to='product.material', verbose_name='материалы'),
        ),
        migrations.AddConstraint(
            model_name='furnituredetails',
            constraint=models.UniqueConstraint(
                fields=('purpose', 'furniture_type', 'construction', 'swing_mechanism', 'armrest_adjustment'),
                name='unique_details',
            ),
        ),
    ]
