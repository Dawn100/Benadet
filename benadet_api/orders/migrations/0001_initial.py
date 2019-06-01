# Generated by Django 2.2.1 on 2019-06-01 09:28

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('start_date', models.DateTimeField(auto_created=True)),
                ('coupon_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('code', models.CharField(max_length=10)),
                ('description', models.TextField(max_length=1000)),
                ('is_active', models.BooleanField(default=False)),
                ('end_date', models.DateTimeField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('is_fulfilled', models.BooleanField(default=False)),
                ('order_date', models.DateTimeField(auto_now_add=True)),
                ('total', models.FloatField()),
                ('coupon_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='orders.Coupon')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='customers.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='Shipping',
            fields=[
                ('shipping_date', models.DateTimeField(auto_created=True)),
                ('shipping_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='ShippingRegion',
            fields=[
                ('shipping_region_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('lat', models.FloatField()),
                ('long', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('transaction_date', models.DateTimeField(auto_created=True)),
                ('transaction_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('code', models.CharField(max_length=100)),
                ('amount', models.FloatField()),
                ('payment_passcode', models.CharField(max_length=50)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='orders.Order')),
            ],
        ),
        migrations.CreateModel(
            name='Tax',
            fields=[
                ('tax_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('tax_pct', models.FloatField()),
                ('amount', models.FloatField()),
                ('tax_name', models.CharField(max_length=250)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.Order')),
                ('shipping', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='orders.Shipping')),
            ],
        ),
        migrations.AddField(
            model_name='shipping',
            name='shipping_region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='orders.ShippingRegion'),
        ),
    ]
