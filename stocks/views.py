import csv, os, subprocess
import matplotlib

from django.shortcuts import render
from django.http import HttpResponse
from django.utils.timezone import make_aware
from datetime import datetime

from .models import Stock, Symbol

def update_db():
  # find all the csv files
  dir = os.getcwd()
  csv_path = '.\stocks\data\\'

  proc = subprocess.Popen(["dir", csv_path, "/b", "/a-d"], stdout=subprocess.PIPE, shell=True)  
  out, err = proc.communicate()
  filenames = out.decode('utf-8').split('\r\n')
  
  for filename in filenames:
    with open(csv_path + filename,"r",encoding="utf-8") as fd, open("updated_dbs.txt","w") as fd_output:
      reader = csv.reader(fd)
      header = next(reader,None) # skip header
      for row in reader:
        stock_date = row[0]
        stock_date_aware = make_aware(datetime.strptime(stock_date, '%Y-%m-%d'))
        if not Stock.objects.filter(symbol=filename[:-4],date=stock_date_aware).exists():
          stock = Stock(symbol=filename[:-4],date=stock_date_aware,stock_open=float(row[1]),stock_high=float(row[2]),stock_low=float(row[3]),stock_close=float(row[4]),stock_adj_close=float(row[5]),volume=int(row[6]))
          stock.save()
          message = filename[:-4] + " @ " + stock_date + " has been uploaded to db."
        else:
          message = filename[:-4] + " @ " + stock_date + " already exists." # stock data already exists
        fd_output.write(message + "\n")

# Create your views here.
def index(request):
  symbol_list = Symbol.objects.order_by('-symbol').reverse()[:10]
  stock_list = Stock.objects.order_by('-symbol').reverse()[:10]
  error_message = ""

  #update_db()

  context = {'first_symbols': symbol_list, 'first_stocks': stock_list}
  context['dir'] = dir
  context['error_message'] = error_message

  
  return render(request, 'stocks/index.html', context)

