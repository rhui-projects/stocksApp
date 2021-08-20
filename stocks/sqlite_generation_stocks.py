import csv
import os
import subprocess
from datetime import datetime
from django.utils.timezone import make_aware

from stocks.models import Symbol, Stock

os.chdir(".\stocks\data")
proc = subprocess.Popen(["dir", "/b"], stdout=subprocess.PIPE, shell=True)
out, err = proc.communicate()
dir_output = out.decode("utf-8")
dirs = dir_output.split("\r\n")

for i in range(len(dirs)):
    if i == 3:
        break
    filename = dirs[i]
    filename
    with open(filename,"r",encoding="utf-8",newline="\n") as fd:
        csvfile = csv.reader(fd,delimiter=",")
        next(csvfile,None) # skip header
        for row in csvfile:
            stock_date = row[0]
            stock_date_aware = make_aware(datetime.strptime(stock_date, '%Y-%m-%d'))
            filename[:-4] + " : " + stock_date
            if not Stock.objects.filter(symbol=filename[:-4],date=stock_date_aware).exists():
                stock = Stock(symbol=filename[:-4],date=stock_date_aware,stock_open=float(row[1]),stock_high=float(row[2]),stock_low=float(row[3]),stock_close=float(row[4]),stock_adj_close=float(row[5]),volume=int(row[6]))
                stock.save()
            else:
                error_message = filename[:-4] + " at date " + stock_date + " already exists"
                error_message