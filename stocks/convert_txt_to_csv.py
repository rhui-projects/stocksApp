import csv
import subprocess
import os

if __name__ == "__main__":
    with open("nasdaqlisted.txt", "r") as nasdaq_file, open("nasdaqlisted.csv","w", newline="",encoding="utf-8") as nasdaq_csv_file:
        os.chdir("data")
        directory = os.getcwd()
        proc = subprocess.Popen(["dir"],stdout=subprocess.PIPE,shell=True)
        out, err = proc.communicate()
        out = out.decode("utf-8")
        csv_reader = csv.reader(nasdaq_file, delimiter="|")
        header = next(csv_reader, None)
        header.append("Saved")
        csv_writer = csv.writer(nasdaq_csv_file, delimiter=",")
        csv_writer.writerow(header)
        for row in csv_reader:
            if row[0] in out:
                csv_writer.writerow(row + ["True"])
            else:
                csv_writer.writerow(row + ["False"])
        
