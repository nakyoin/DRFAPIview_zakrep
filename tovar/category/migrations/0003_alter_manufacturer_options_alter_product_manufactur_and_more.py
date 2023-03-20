# Generated by Django 4.1.6 on 2023-03-17 22:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0002_manufacturer_product_delete_men'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='manufacturer',
            options={'verbose_name': 'Manufacturer', 'verbose_name_plural': 'Manufacturers'},
        ),
        migrations.AlterField(
            model_name='product',
            name='manufactur',
            field=models.CharField(default='Безымянный', max_length=255),
        ),
        migrations.AlterField(
            model_name='product',
            name='size',
            field=models.TextField(default='Неизвестно'),
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('total_price', models.IntegerField(default=0)),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='category.product')),
            ],
            options={
                'verbose_name': 'Cart',
                'verbose_name_plural': 'Carts',
            },
        ),
    ]
