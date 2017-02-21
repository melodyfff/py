import csv
with open('common.csv','r',encoding='GBK') as csvfile:
     reader = csv.reader(csvfile)
     rows = [row for row in reader]
     print(rows)
