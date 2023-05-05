import requests
from bs4 import BeautifulSoup
from requests import ReadTimeout
import csv
import pandas as pd


csv_file = open('getinfo2.csv', 'a+', newline='')
csv_writer = csv.writer(csv_file)
csv_file2 = open('errorlinks2.csv', 'a+', newline='')
csv_writer2 = csv.writer(csv_file2)

begRow=59331#跳过表格的前begRow行
redRow=668#读取redRow条数据
def get_movie_id(movie_csv_path):
    movie_dct = {}
    df=pd.read_csv(movie_csv_path,skiprows=begRow-1,nrows=redRow)
    lines=df.values.tolist()
    for i in range(len(lines)):
        str_line=int(lines[i][1])
        str_line=str(str_line)
        index=int(lines[i][0])
        index=str(index)
        movie_dct[index]=str_line
    return movie_dct

if __name__ == "__main__":

    url = 'https://www.imdb.com/title/tt'

    cur_movie_id = None
    cur_imdb_id = None


    # 存放每一步电影的id和imdb的id
    movie_dct = get_movie_id(r"D:\个人\学习\大三下\数据可视化\实验\大作业\ml-25m\links.csv")
    count=0
    for movie_id, imdb_id in movie_dct.items():
        count=count+1
        countall=count+begRow
        print("现在开始读取第{}条数据".format(countall))
        country = None
        cur_movie_id = movie_id
        cur_imdb_id = imdb_id
        addZeroNum = 7-len(str(cur_imdb_id))
        if addZeroNum == 0:
            URL = url + cur_imdb_id
        elif addZeroNum == 1:
            URL = url + '0' + cur_imdb_id
        elif addZeroNum == 2:
            URL = url + '00' + cur_imdb_id
        elif addZeroNum == 3:
            URL = url + '000' + cur_imdb_id
        elif addZeroNum == 4:
            URL = url + '0000' + cur_imdb_id
        elif addZeroNum == 5:
            URL = url + '00000' + cur_imdb_id
        elif addZeroNum == 6:
            URL = url + '000000' + cur_imdb_id

        print(URL)

        try:
            strhtml = requests.get(URL, timeout=30)  # Get方式获取网页数据
            if strhtml.status_code == 200:
                print('correct')
            else:
                print('error')
                csv_writer2.writerow([cur_movie_id, cur_imdb_id])  # 将数据存入csv文件
                continue
            soup = BeautifulSoup(strhtml.text, 'lxml')
            for i, tags in enumerate(soup.find_all(class_='txt-block')):
                for h4 in tags.find_all('h4'):
                    title = h4.get_text()  # 例如Director
                    # print(title)
                    if title == 'Country:':
                        for _, a in enumerate(h4.next_siblings):
                            if a.name == 'a':
                                country = a.get_text()
            print(country)

        except (ConnectionError, ReadTimeout):
            print('Crawling Failed', URL)
            csv_writer2.writerow([cur_movie_id, cur_imdb_id])  # 将数据存入csv文件
            continue
        except:
            print(cur_movie_id + 'is error')
            csv_writer2.writerow([cur_movie_id, cur_imdb_id])  # 将数据存入csv文件
            continue
        if country==None:
            csv_writer2.writerow([cur_movie_id, cur_imdb_id])
            print("country is None")
        else:
            print(cur_movie_id, cur_imdb_id, country)
            csv_writer.writerow([cur_movie_id, cur_imdb_id, country])  # 将数据存入csv文件
    csv_file.close()  # 关闭csv文件