# Generated by Django 2.2.1 on 2019-06-01 09:28

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('discount_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('discount_pct', models.FloatField(blank=True)),
                ('discount_amount', models.FloatField(blank=True)),
                ('description', models.CharField(max_length=1000)),
                ('product', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='products.Product')),
            ],
        ),
    ]
