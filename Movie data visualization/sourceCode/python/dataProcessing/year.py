import requests
from bs4 import BeautifulSoup
from requests import ReadTimeout
import csv
import pandas as pd
import time,datetime

#创建写入的文件
csv_writer=[1]*25
yearBegin = 1995
for i in range(0,25):
    file = str(yearBegin) + ".csv"
    csv_file=open(file, 'a+', newline='')
    csv_writer[i]=csv.writer((csv_file))
    yearBegin=yearBegin+1

#开始按时间选取
timeBegin=[]
timeEnd=[]

begRow=2#跳过表格的前begRow行

path=r"D:\个人\学习\大三下\数据可视化\实验\大作业\ml-25m\ratings.csv";
count=begRow;
df = pd.read_csv(path, skiprows=begRow - 1, chunksize=1000)
for chunk in df:
    lines = chunk.values.tolist()
    for i in range(len(lines)):
        count=count+1
        print("现在开始读取第{}行".format(count))
        timeStamp = int(lines[i][3])
        timeArray = time.localtime(timeStamp)
        timecsv = timeArray[0] - 1995
        csv_writer[timecsv].writerow(lines[i][:])
print("结束")
csv_file.close()  # 关闭csv文件

