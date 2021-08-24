# Generated by Django 3.2.6 on 2021-08-19 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('stock_id', models.AutoField(primary_key=True, serialize=False)),
                ('symbol', models.CharField(max_length=8)),
                ('date', models.DateTimeField(verbose_name='Date')),
                ('stock_open', models.DecimalField(decimal_places=6, max_digits=10, verbose_name='Open')),
                ('stock_high', models.DecimalField(decimal_places=6, max_digits=10, verbose_name='High')),
                ('stock_low', models.DecimalField(decimal_places=6, max_digits=10, verbose_name='Low')),
                ('stock_close', models.DecimalField(decimal_places=6, max_digits=10, verbose_name='Close')),
                ('stock_adj_close', models.DecimalField(decimal_places=6, max_digits=10, verbose_name='Adj Close')),
                ('volume', models.BigIntegerField(db_column='Volume')),
            ],
        ),
        migrations.CreateModel(
            name='Symbol',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symbol', models.CharField(max_length=10, unique=True)),
                ('security', models.CharField(max_length=100)),
                ('market', models.CharField(max_length=1)),
                ('test', models.CharField(max_length=1)),
                ('status', models.CharField(max_length=1)),
                ('shares', models.IntegerField(default=0)),
                ('etf', models.CharField(max_length=1)),
                ('nextShares', models.CharField(max_length=1)),
            ],
        ),
    ]