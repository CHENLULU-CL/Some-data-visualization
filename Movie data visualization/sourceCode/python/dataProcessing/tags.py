import requests
from bs4 import BeautifulSoup
from requests import ReadTimeout
import csv
import pandas as pd
import heapq

csv_file = open('tags.csv', 'a+', newline='')
csv_writer = csv.writer(csv_file)

path = r"D:\个人\学习\大三下\数据可视化\实验\大作业\ml-25m\genome-scores.csv"
path_tag=r"D:\个人\学习\大三下\数据可视化\实验\大作业\ml-25m\genome-tags.csv"
df = pd.read_csv(path, encoding='gbk', chunksize=1128)
df_tag=pd.read_csv(path_tag,encoding='gbk')
tags=df_tag.values.tolist()
# print(tags)

for chunk in df:
    lines =chunk.values
    # print(lines)
    scores=lines[:,2].tolist()
    # print(scores)
    max_scores=heapq.nlargest(5,scores)
    # print(max_scores)
    index_scores=list(map(scores.index,heapq.nlargest(5,scores)))
    # print(list(index_scores))
    #在tag中根据index搜索对应的tag
    newtags=[int(lines[0,0])]
    print("现在读取id为{}的电影标签".format(newtags[0]))
    for i in range(5):
        tag=tags[index_scores[i]][1]
        newtags.append(tag)
    #写入文件
    csv_writer.writerow(newtags)

csv_file.close()  # 关闭csv文件
