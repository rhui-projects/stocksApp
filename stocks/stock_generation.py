import pandas as pd
from ftplib import FTP
import subprocess
from time import time, sleep
from contextlib import closing
import csv
import urllib.request
import os


def download_stock(tickers):
  for i in range(len(tickers)):
    filename = "data/" + tickers[i] + ".csv"

    if os.path.isfile(filename):
      continue
    url = "https://query1.finance.yahoo.com/v7/finance/download/" + tickers[i]
    url += "?period1=0&period2=" + str(int(time()))  
    try:
      response = urllib.request.urlopen(url)
    except:
      continue

    lines = [l.decode("utf-8") for l in response.readlines()]
    with open(filename, "w") as fd: 
      for line in lines:
        fd.write(line)

def download_tickers():
  with FTP('ftp.nasdaqtrader.com') as ftp:
    print(ftp.login())
    ftp.cwd('Symboldirectory')
    #ftp.retrlines('LIST')
    with open('nasdaqlisted.txt','wb') as fd:
      print(ftp.retrbinary('RETR nasdaqlisted.txt', fd.write))


def main():
  proc = subprocess.Popen(["ls"], stdout=subprocess.PIPE, shell=True)
  out, err = proc.communicate()
  
  # Download stock tickers if the do not exist locally
  if 'nasdaqlisted.txt' not in out.decode('utf-8'):
    download_tickers()
  
  
  data = pd.read_csv('nasdaqlisted.txt',delimiter="|",header=0)
  tickers = (data.iloc[:,0]).values.tolist()

  download_stock(tickers)


if __name__ == "__main__":
  main() 