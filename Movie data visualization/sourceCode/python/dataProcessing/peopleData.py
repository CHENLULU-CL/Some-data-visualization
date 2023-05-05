import csv
import pandas as pd



def findCountry(id):
    country_path = r"D:\个人\学习\大三下\数据可视化\大作业\数据处理\country.csv"
    dfcounty = pd.read_csv(country_path, encoding='utf-8', chunksize=500, header=None)
    for chunk_country in dfcounty:
        lines_country=chunk_country.values
        if id in lines_country[:,0]:
            index_country=lines_country[:,0].tolist().index(id)
            country=lines_country[index_country][2]
            #获取country.csv中的国家信息
            return country
    print("未找 国家信息")
    return 0

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
    return 0

def findPingfen(id):
    pingfen_path = r"D:\个人\学习\大三下\数据可视化\大作业\数据处理\1995-2019pingfen\pingfen{}.csv"
    newfen = []
    for year in range(1995,2020):
        isok = False
        fen_path=pingfen_path.format(year)
        dffen=pd.read_csv(fen_path,encoding='utf-8',chunksize=500)
        for chunk_fen in dffen:
            lines_fen=chunk_fen.values
            if id in lines_fen[:,0]:
                index_fen=lines_fen[:,0].tolist().index(id)
                # print(index_fen)
                newfen.append(lines_fen[index_fen][1])
                newfen.append(lines_fen[index_fen][2])
                # print(newfen)
                isok=True
                break
        if(not isok):
            newfen.extend([0, 0])
        # print("year{} newfen{}".format(year,newfen))
    # print(newfen)
    return newfen


#电影id，电影名称，生产年份，国家，类型，每年评分，及平均评分

if __name__ == "__main__":
    movie_path=r"D:\个人\学习\大三下\数据可视化\大作业\数据处理\year.csv"

    people_path = r"D:\个人\学习\大三下\数据可视化\大作业\数据处理\people.csv"
    csv_fileP = open(people_path, 'a+', newline='')
    csv_writerP = csv.writer(csv_fileP)

    csv_writerP.writerow(["movieID","name","year","country","types","1995score","1995users","1996score","1996users"
                          ,"1997score","1997users","1998score","1998users","1999score","1999users","2000score","2000users"
                          ,"2001score","2001users","2002score","2002users","2003score","2003users","2004score","2004users"
                          ,"2005score","2005users","2006score","2006users","2007score","2007users","2008score","2008users"
                          ,"2009score","2009users","2010score","2010users","2011score","2011users","2012score","2012users"
                          ,"2013score","2013users","2014score","2014users","2015score","2015users","2016score","2016users"
                          ,"2017score","2017users","2018score","2018users","2019score","2019users"])

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
                newline = lines_movie[i]
                # 获取电影国家信息
                country = findCountry(mid)
                newline.append(country)
                # 获取类型信息
                mtype = findType(mid)
                newline.append(mtype)
                # 获取每年评分信息
                fen = findPingfen(mid)
                newline.extend(fen)
                # 写入表格
                csv_writerP.writerow(newline)
                print(newline)
            except:
                print("error")
    csv_fileP.close()
    print("over")