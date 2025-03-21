# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-06-13 20:58
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('organ', '0001_initial'),
        ('basedata', '0001_initial'),
        ('selfhelp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('begin', models.DateField(blank=True, null=True, verbose_name='begin date')),
                ('end', models.DateField(blank=True, null=True, verbose_name='end date')),
                ('creator', models.CharField(blank=True, max_length=20, null=True, verbose_name='creator')),
                ('modifier', models.CharField(blank=True, max_length=20, null=True, verbose_name='modifier')),
                ('creation', models.DateTimeField(auto_now_add=True, null=True, verbose_name='creation')),
                ('modification', models.DateTimeField(auto_now=True, null=True, verbose_name='modification')),
                ('vo_date', models.DateField(blank=True, default=datetime.date.today, null=True, verbose_name='invoice date')),
                ('code', models.CharField(max_length=20, verbose_name='invoice code')),
                ('number', models.CharField(max_length=20, verbose_name='invoice number')),
                ('po_amount', models.DecimalField(blank=True, decimal_places=4, max_digits=14, null=True, verbose_name='po amount')),
                ('vo_amount', models.DecimalField(decimal_places=4, max_digits=14, verbose_name='invoice amount')),
                ('file', models.FileField(blank=True, null=True, upload_to=b'invoice', verbose_name='invoice file')),
                ('partner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='basedata.Partner', verbose_name='partner')),
            ],
            options={
                'verbose_name': 'Invoice',
                'verbose_name_plural': 'Invoice',
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('begin', models.DateField(blank=True, null=True, verbose_name='begin date')),
                ('end', models.DateField(blank=True, null=True, verbose_name='end date')),
                ('creator', models.CharField(blank=True, max_length=20, null=True, verbose_name='creator')),
                ('modifier', models.CharField(blank=True, max_length=20, null=True, verbose_name='modifier')),
                ('creation', models.DateTimeField(auto_now_add=True, null=True, verbose_name='creation')),
                ('modification', models.DateTimeField(auto_now=True, null=True, verbose_name='modification')),
                ('py_date', models.DateField(blank=True, default=datetime.date.today, null=True, verbose_name='pay date')),
                ('code', models.CharField(blank=True, max_length=20, null=True, verbose_name='pay code')),
                ('po_amount', models.DecimalField(blank=True, decimal_places=4, max_digits=14, null=True, verbose_name='po amount')),
                ('py_amount', models.DecimalField(decimal_places=4, max_digits=14, verbose_name='pay amount')),
                ('response_code', models.CharField(blank=True, max_length=80, null=True, verbose_name='response code')),
                ('memo', models.TextField(blank=True, null=True, verbose_name='memo')),
                ('bank', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='basedata.BankAccount', verbose_name='bank account')),
                ('org', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='organ.Organization', verbose_name='organization')),
                ('partner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='basedata.Partner', verbose_name='partner')),
            ],
            options={
                'verbose_name': 'Payment',
                'verbose_name_plural': 'Payment',
            },
        ),
        migrations.CreateModel(
            name='POItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(blank=True, decimal_places=4, max_digits=12, null=True, verbose_name='price')),
                ('cnt', models.DecimalField(blank=True, decimal_places=4, max_digits=12, null=True, verbose_name='count')),
                ('discount_price', models.DecimalField(blank=True, decimal_places=4, max_digits=12, null=True, verbose_name='discount price')),
                ('amount', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True, verbose_name='money of amount')),
                ('discount_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True, verbose_name='discount amount')),
                ('tax', models.CharField(default=b'0.00', max_length=6, verbose_name='tax rate')),
                ('is_in_stock', models.BooleanField(default=0, verbose_name='is in stock')),
                ('in_stock_time', models.DateTimeField(blank=True, null=True, verbose_name='execute time')),
                ('entry_cnt', models.DecimalField(blank=True, decimal_places=4, max_digits=12, null=True, verbose_name='entry count')),
                ('left_cnt', models.DecimalField(blank=True, decimal_places=4, max_digits=12, null=True, verbose_name='left count')),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='basedata.Material', verbose_name='material')),
                ('measure', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='basedata.Measure', verbose_name='measure')),
            ],
            options={
                'verbose_name': 'po item',
                'verbose_name_plural': 'po item',
            },
        ),
        migrations.CreateModel(
            name='PurchaseOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('begin', models.DateField(blank=True, null=True, verbose_name='begin date')),
                ('end', models.DateField(blank=True, null=True, verbose_name='end date')),
                ('creator', models.CharField(blank=True, max_length=20, null=True, verbose_name='creator')),
                ('modifier', models.CharField(blank=True, max_length=20, null=True, verbose_name='modifier')),
                ('creation', models.DateTimeField(auto_now_add=True, null=True, verbose_name='creation')),
                ('modification', models.DateTimeField(auto_now=True, null=True, verbose_name='modification')),
                ('code', models.CharField(blank=True, max_length=20, null=True, verbose_name='code')),
                ('order_date', models.DateField(verbose_name='order date')),
                ('arrive_date', models.DateField(verbose_name='arrive date')),
                ('title', models.CharField(max_length=40, verbose_name='title')),
                ('description', models.TextField(blank=True, null=True, verbose_name='description')),
                ('status', models.CharField(choices=[(b'0', 'NEW'), (b'1', 'IN PROGRESS'), (b'4', 'DROP'), (b'9', 'APPROVED'), (b'99', 'ALREADY STOCK IN')], default=b'0', max_length=2, verbose_name='status')),
                ('amount', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=12, null=True, verbose_name='money amount')),
                ('discount_amount', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=12, null=True, verbose_name='discount amount')),
                ('entry_status', models.BooleanField(default=0, verbose_name='entry status')),
                ('entry_time', models.DateTimeField(blank=True, null=True, verbose_name='entry time')),
                ('attach', models.FileField(blank=True, help_text='\u60a8\u53ef\u5bfc\u5165\u91c7\u8d2d\u660e\u7ec6\uff0c\u6a21\u677f\u8bf7\u53c2\u8003\u6587\u6863FD0008', null=True, upload_to=b'', verbose_name='attach')),
                ('org', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='organ.Organization', verbose_name='organization')),
                ('partner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='basedata.Partner', verbose_name='partner')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'verbose_name': 'purchase order',
                'verbose_name_plural': 'purchase orders',
            },
        ),
        migrations.AddField(
            model_name='poitem',
            name='po',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='purchase.PurchaseOrder', verbose_name='purchase order'),
        ),
        migrations.AddField(
            model_name='poitem',
            name='woitem',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='selfhelp.WOItem', verbose_name='wo item'),
        ),
        migrations.AddField(
            model_name='payment',
            name='po',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='purchase.PurchaseOrder', verbose_name='purchase order'),
        ),
        migrations.AddField(
            model_name='invoice',
            name='po',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='purchase.PurchaseOrder', verbose_name='purchase order'),
        ),
    ]
