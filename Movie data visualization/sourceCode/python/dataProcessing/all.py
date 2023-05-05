# coding: utf-8

import requests
from bs4 import BeautifulSoup
from requests import ReadTimeout
import csv
import pandas as pd


# filename=r"gaofen1995.csv"
# csv_file = open(filename, 'a+', newline='')
# csv_writer = csv.writer(csv_file)

def findCountry(id):
    country_path = r"D:\个人\学习\大三下\数据可视化\大作业\数据处理\country.csv"
    dfcounty = pd.read_csv(country_path, encoding='utf-8', chunksize=500, header=None)
    for chunk_country in dfcounty:
        lines_country=chunk_country.values
        if id in lines_country[:,0]:
            # print("country find")
            index_country=lines_country[:,0].tolist().index(id)
            country=lines_country[index_country][2]
            #获取country.csv中的国家信息
            return country
    print("未找 国家信息")
    return None

def findType(id):
    type_path = r"D:\个人\学习\大三下\数据可视化\实验\大作业\ml-25m\movies.csv"
    dftype = pd.read_csv(type_path, encoding='utf-8', chunksize=500)
    for chunk_type in dftype:
        lines_type=chunk_type.values
        if id in lines_type[:,0]:
            # print("type find")
            index_type=lines_type[:,0].tolist().index(id)
            type=lines_type[index_type][2]
            #获取country.csv中的国家信息
            return type
    print("未找 类型信息")
    return None

def findTags(id):
    tag_path = r"D:\个人\学习\大三下\数据可视化\大作业\数据处理\tags.csv"
    dftag = pd.read_csv(tag_path, encoding='utf-8',chunksize=500, header=None)
    for chunk_tag in dftag:
        lines_tag=chunk_tag.values
        if id in lines_tag[:,0]:
            # print("type find")
            index_tag=lines_tag[:,0].tolist().index(id)
            tag = lines_tag[index_tag][1:]
            #获取tags.csv中的标签
            return tag
    print("未找 标签信息")
    return None

def findYear(id):
    year_path = r"D:\个人\学习\大三下\数据可视化\大作业\数据处理\year.csv"
    dfyear = pd.read_csv(year_path, encoding='gbk', chunksize=500, header=None)
    for chunk_year in dfyear:
        lines_year=chunk_year.values
        if id in lines_year[:,0]:
            # print("type find")
            index_year=lines_year[:,0].tolist().index(id)
            year = lines_year[index_year][1:]
            #获取tags.csv中的标签
            return year
    print("未找 年份信息")
    return None


if __name__ == "__main__":
    begRow = 0  # 跳过表格的前begRow行
    # redRow=668#读取redRow条数据
    locat_path = r"D:\个人\学习\大三下\数据可视化\大作业\数据处理\1995-2019gaofen\gaofen2019.csv"

    new_path=r"D:\个人\学习\大三下\数据可视化\大作业\数据处理\1995-2019gaofenALL\G2019A.csv"
    csv_file = open(new_path, 'a+', newline='')
    csv_writer = csv.writer(csv_file)

    error_path = r"D:\个人\学习\大三下\数据可视化\大作业\数据处理\1995-2019gaofenALL\G2019A_error.csv"
    csv_fileE = open(error_path, 'a+', newline='')
    csv_writerE = csv.writer(csv_fileE)

    notag_path = r"D:\个人\学习\大三下\数据可视化\大作业\数据处理\1995-2019gaofenALL\G2019A_notag.csv"
    csv_fileN = open(notag_path, 'a+', newline='')
    csv_writerN = csv.writer(csv_fileN)

    df = pd.read_csv(locat_path, encoding='utf-8', chunksize=500,header=None)

    count=0

    for chunk in df:
        lines=chunk.values.tolist()
        for i in range(len(lines)):
            count=count+1;
            mid = int(lines[i][0])
            print("现在开始读取第{}条电影id{}".format(count,mid))
            # id/名称/电影年份/国家/类型/评分/评分人数/标签/评分与生产时间间隔
            # mid = 1
            newline = []
            #电影id
            newline.append(mid)
            # print(newline)
            # 获取year.csv中电影的年份信息
            try:
                year_info = findYear(mid)
                newline.extend(year_info)
                # 获取counry,csv中的国家信息
                country_info = findCountry(mid)
                newline.append(country_info)
                # 获取movies.csv中的电影类型信息
                type_info = findType(mid)
                newline.append(type_info)
                # 获取高低分.csv中的分数信息 平均分，评分人数
                newline.append(lines[i][2])
                newline.append(lines[i][3])
            except:
                csv_writerE.writerow([mid])
                print("电影id：{}信息查找错误".format(mid))
                continue

            # 获取处理后的tags.csv中电影标签信息
            try:
                tag_info = findTags(mid)
                newline.extend(tag_info)
            except:
                print(newline)
                csv_writerN.writerow(newline)
                continue
            print(newline)
            # 写入新的表格中
            csv_writer.writerow(newline)

    print("over")
    csv_file.close()  # 关闭csv文件
    csv_fileE.close()
    csv_fileN.close()


# def get_movie_id(movie_csv_path):
#     movie_dct = {}
#
#     lines=df.values.tolist()
#     for i in range(len(lines)):
#         str_line=int(lines[i][1])
#         str_line=str(str_line)
#         index=int(lines[i][0])
#         index=str(index)
#         movie_dct[index]=str_line
#     return movie_dct
#
# if __name__ == "__main__":
#
#     url = 'https://www.imdb.com/title/tt'
#
#     cur_movie_id = None
#     cur_imdb_id = None
#
#
#     # 存放每一步电影的id和imdb的id
#     movie_dct = get_movie_id(r"D:\个人\学习\大三下\数据可视化\实验\大作业\ml-25m\links.csv")
#     count=0
#     for movie_id, imdb_id in movie_dct.items():
#         count=count+1
#         countall=count+begRow
#         print("现在开始读取第{}条数据".format(countall))
#         country = None
#         cur_movie_id = movie_id
#         cur_imdb_id = imdb_id
#         addZeroNum = 7-len(str(cur_imdb_id))
#         if addZeroNum == 0:
#             URL = url + cur_imdb_id
#         elif addZeroNum == 1:
#             URL = url + '0' + cur_imdb_id
#         elif addZeroNum == 2:
#             URL = url + '00' + cur_imdb_id
#         elif addZeroNum == 3:
#             URL = url + '000' + cur_imdb_id
#         elif addZeroNum == 4:
#             URL = url + '0000' + cur_imdb_id
#         elif addZeroNum == 5:
#             URL = url + '00000' + cur_imdb_id
#         elif addZeroNum == 6:
#             URL = url + '000000' + cur_imdb_id
#
#         print(URL)
#
#         try:
#             strhtml = requests.get(URL, timeout=30)  # Get方式获取网页数据
#             if strhtml.status_code == 200:
#                 print('correct')
#             else:
#                 print('error')
#                 csv_writer2.writerow([cur_movie_id, cur_imdb_id])  # 将数据存入csv文件
#                 continue
#             soup = BeautifulSoup(strhtml.text, 'lxml')
#             for i, tags in enumerate(soup.find_all(class_='txt-block')):
#                 for h4 in tags.find_all('h4'):
#                     title = h4.get_text()  # 例如Director
#                     # print(title)
#                     if title == 'Country:':
#                         for _, a in enumerate(h4.next_siblings):
#                             if a.name == 'a':
#                                 country = a.get_text()
#             print(country)
#
#         except (ConnectionError, ReadTimeout):
#             print('Crawling Failed', URL)
#             csv_writer2.writerow([cur_movie_id, cur_imdb_id])  # 将数据存入csv文件
#             continue
#         except:
#             print(cur_movie_id + 'is error')
#             csv_writer2.writerow([cur_movie_id, cur_imdb_id])  # 将数据存入csv文件
#             continue
#         if country==None:
#             csv_writer2.writerow([cur_movie_id, cur_imdb_id])
#             print("country is None")
#         else:
#             print(cur_movie_id, cur_imdb_id, country)
#             csv_writer.writerow([cur_movie_id, cur_imdb_id, country])  # 将数据存入csv文件
#     csv_file.close()  # 关闭csv文件