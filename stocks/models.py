from django.db import models

# Create your models here.
class Symbol(models.Model):
  symbol = models.CharField(max_length=10)
  security = models.CharField(max_length=100)
  market = models.CharField(max_length=1)
  test = models.CharField(max_length=1)
  status = models.CharField(max_length=1)
  shares = models.IntegerField(default=0)
  etf = models.CharField(max_length=1)
  nextShares = models.CharField(max_length=1)

  def __str__(self):
    return self.symbol

class Stock(models.Model):
  symbol = models.ForeignKey(Symbol, on_delete=models.CASCADE)
  date = models.DateTimeField('Date')
  stock_open = models.DecimalField('Open',decimal_places=6,max_digits=10)
  stock_high = models.DecimalField('High',decimal_places=6,max_digits=10)
  stock_low = models.DecimalField('Low',decimal_places=6,max_digits=10)
  stock_close = models.DecimalField('Close',decimal_places=6,max_digits=10)
  stock_adj_close = models.DecimalField('Adj Close',decimal_places=6,max_digits=10)
  volume = models.BigIntegerField(db_column='Volume')

  def __str__(self):
    return self.symbol
  

