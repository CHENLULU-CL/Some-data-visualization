import csv
import pandas as pd

#电影id，电影名称，生产年份，国家，类型，每年评分，及平均评分

if __name__ == "__main__":
    movie_path=r"D:\个人\学习\大三下\数据可视化\大作业\数据处理\people2.csv"

    people_path = r"D:\个人\学习\大三下\数据可视化\大作业\数据处理\people_top.csv"
    csv_fileP = open(people_path, 'a+', newline='')
    csv_writerP = csv.writer(csv_fileP)
    countrylist=['USA','UK','France','China']

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
            try:
                if lines_movie[i][3] in countrylist:
                    csv_writerP.writerow(lines_movie[i])
                    print(lines_movie[i])
            except:
                print("error")
    csv_fileP.close()
    print("over")