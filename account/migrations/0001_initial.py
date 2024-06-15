# Generated by Django 5.0.6 on 2024-06-15 14:09

import django.core.validators
import django.db.models.deletion
import phonenumber_field.modelfields
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TransactionModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_no', models.CharField(default=uuid.uuid4, max_length=50, unique=True)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('checkout_request_id', models.CharField(max_length=200)),
                ('reference', models.CharField(blank=True, max_length=40)),
                ('description', models.TextField(blank=True, null=True)),
                ('amount', models.CharField(max_length=10)),
                ('status', models.CharField(choices=[(1, 'Pending'), (0, 'Complete')], default=1, max_length=15)),
                ('receipt_no', models.CharField(blank=True, max_length=200, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('ip', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='BillingAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('pin_code', models.CharField(max_length=6, validators=[django.core.validators.RegexValidator('^\\d{0,9}$')])),
                ('house_no', models.CharField(max_length=300)),
                ('landmark', models.CharField(max_length=120)),
                ('city', models.CharField(max_length=120)),
                ('state', models.CharField(max_length=120)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='billingmodel', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrderModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=120)),
                ('email', models.EmailField(max_length=254)),
                ('ordered_item', models.CharField(blank=True, default='Not Set', max_length=200, null=True)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('address', models.CharField(blank=True, max_length=300, null=True)),
                ('paid_status', models.BooleanField(default=False)),
                ('paid_at', models.DateTimeField(blank=True, null=True)),
                ('total_price', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('is_delivered', models.BooleanField(default=False)),
                ('delivered_at', models.CharField(blank=True, max_length=200, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
