import csv
import os
import subprocess
from datetime import datetime

from stocks.models import Symbol, Stock

os.chdir("stocks")
proc = subprocess.Popen(["dir"], stdout=subprocess.PIPE, shell=True)
out, err = proc.communicate()
dir_output = out.decode("utf-8")
dirs = dir_output.split("\r\n")

with open("nasdaqlisted.csv","r", encoding="utf-8") as fd:
    csvfile = csv.reader(fd)
    next(csvfile,None) # skip header
    for row in csvfile:
        if "File Creation Time:" in row[0]:
            break
        symbol = Symbol(symbol=row[0],security=row[1],market=row[2],test=row[3],status=row[4],shares=row[5],etf=row[6],nextShares=row[7])
        symbol.save()