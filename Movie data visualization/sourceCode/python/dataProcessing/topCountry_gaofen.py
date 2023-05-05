import csv
import pandas as pd

#电影id，电影名称，生产年份，国家，类型，每年评分，及平均评分
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

if __name__ == "__main__":
    movie_path=r"D:\个人\学习\大三下\数据可视化\大作业\数据处理\people_top.csv"

    people_path = r"D:\个人\学习\大三下\数据可视化\大作业\数据处理\topCountry_gaofen.csv"
    people2_path = r"D:\个人\学习\大三下\数据可视化\大作业\数据处理\topCountry_difen.csv"
    csv_fileP = open(people_path, 'a+', newline='')
    csv_writerP = csv.writer(csv_fileP)
    csv_fileP2 = open(people2_path, 'a+', newline='')
    csv_writerP2 = csv.writer(csv_fileP2)


    dfmovie=pd.read_csv(movie_path,encoding='gbk',chunksize=500,header=None)
    count=0;
    newline=[]
    for chunk_movie in dfmovie:
        lines_movie=chunk_movie.values.tolist()
        for i in range(len(lines_movie)):
            count=count+1
            mid=lines_movie[i][0]
            print("现在开始读取第 {} 条电影id {} 信息".format(count,mid))
            #获取年份等信息
            scoreall = 0;
            personall=0;
            newline = lines_movie[i]
            # 按照分数/人气
            for k in range(5, 54, 2):
                # print(k)
                score = lines_movie[i][k]
                person = lines_movie[i][k + 1]
                personall = personall + person
                scoreall = scoreall + score * person
            if personall==0:
                continue
            average = scoreall / personall
            if average>= 4:
                tags=findTags(mid)
                newline.extend([average, personall])
                if type(tags)!=type(None):
                    newline.extend(tags)
                csv_writerP.writerow(newline)
            elif average<=2:
                tags = findTags(mid)
                newline.extend([average, personall])
                # print(type(tags))
                if type(tags)!=type(None):
                    newline.extend(tags)
                csv_writerP2.writerow(newline)
    csv_fileP.close()
    csv_fileP2.close()
    print("over")