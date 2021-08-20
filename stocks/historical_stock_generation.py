'''
Script:       historical_stock_generation.py
Author:       Ryan Hui
Description:  This script is used to download historical stock data from companies within NASDAQ.
              All historical data are stored in the data folder as csv files.
              
'''

from ftplib import FTP
import subprocess
from time import time, sleep
import csv
import urllib.request
import os


def download_stock():
  downloaded = [] # contains downloaded historical stock data
  f_reader = open("nasdaqlisted.csv","r",encoding="utf-8")
  reader = csv.reader(f_reader)
  row = next(reader,None)
  print(row)
  f_writer = open("nasdaqlisted_saved_status.csv","w",newline="",encoding="utf-8")
  writer = csv.writer(f_writer)
  writer.writerow(row) # header
  for row in reader:
    filename = "data/" + row[0] + ".csv"
    if os.path.isfile(filename):
      print("Already downloaded " + row[0])
      row[-1] = "True"
      writer.writerow(row)
      continue
    
    url = "https://query1.finance.yahoo.com/v7/finance/download/" + row[0]
    url += "?period1=0&period2=" + str(int(time()))

    try:
      # test if url exists for tickers[i]
      response = urllib.request.urlopen(url)
      downloaded.append(row[0])

      # Download historical csv data for tickers[i]
      lines = [l.decode("utf-8") for l in response.readlines()]
      with open(filename, "w") as fd:
        for line in lines:
          fd.write(line)
      print("Just downloaded " + row[0])

      # Update "nasdaqlisted.csv"
      row[-1] = "True"
      writer.writerow(row)

    except:
      print("ERROR: Cannot download: " + row[0])
      writer.writerow(row)
      continue

  f_reader.close()
  f_writer.close()

def download_tickers():
  with FTP('ftp.nasdaqtrader.com') as ftp:
    print(ftp.login())
    ftp.cwd('Symboldirectory')
    #ftp.retrlines('LIST')
    with open('nasdaqlisted.txt','wb') as fd:
      print(ftp.retrbinary('RETR nasdaqlisted.txt', fd.write))


def main():
  proc = subprocess.Popen(["dir"], stdout=subprocess.PIPE, shell=True)
  out, err = proc.communicate()
  print(os.getcwd())
  
  # Download stock tickers if the do not exist locally
  if 'nasdaqlisted.txt' not in out.decode('utf-8'):
    download_tickers()
  
  download_stock()


if __name__ == "__main__":
  main() 
