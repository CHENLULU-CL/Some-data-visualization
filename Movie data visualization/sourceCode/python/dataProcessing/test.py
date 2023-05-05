import requests
from bs4 import BeautifulSoup
from requests import ReadTimeout
import csv
import pandas as pd


locat_path = r"D:\个人\学习\大三下\数据可视化\实验\大作业\ml-25m\links.csv"
df = pd.read_csv(locat_path, encoding='gbk', chunksize=2)
for chunk_country in df:
    lines_country = chunk_country.values
    print(lines_country)
    break


