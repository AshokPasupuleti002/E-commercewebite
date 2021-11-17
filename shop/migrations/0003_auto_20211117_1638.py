# Generated by Django 3.2.9 on 2021-11-17 11:08

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_order'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name': 'Order'},
        ),
        migrations.AlterModelOptions(
            name='products',
            options={'verbose_name': 'Product'},
        ),
        migrations.AddField(
            model_name='order',
            name='total',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]
