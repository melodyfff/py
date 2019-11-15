# coding=utf-8
# 读取csv文件

import csv

with open('common.csv', 'r', encoding='GBK') as csv_file:
    reader = csv.reader(csv_file)
    rows = [row for row in reader]
    print(rows)
