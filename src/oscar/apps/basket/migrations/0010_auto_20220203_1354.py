# Generated by Django 3.2.9 on 2022-02-03 08:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('basket', '0009_line_date_updated'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('basket_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='basket.basket')),
                ('schema_name', models.CharField(max_length=255, verbose_name='vendor_schema_name')),
                ('domain', models.CharField(max_length=255, verbose_name='vendor_domain')),
            ],
            options={
                'verbose_name': 'Basket',
                'verbose_name_plural': 'Baskets',
                'abstract': False,
            },
            bases=('basket.basket',),
        ),
        migrations.AlterField(
            model_name='basket',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='line',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='lineattribute',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
