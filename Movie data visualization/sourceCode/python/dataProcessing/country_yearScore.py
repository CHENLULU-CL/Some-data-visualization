import csv
import pandas as pd

if __name__ == "__main__":
    new_path=r"D:\个人\学习\大三下\数据可视化\大作业\数据处理\country_France_difen.csv"

    people_path = r"D:\个人\学习\大三下\数据可视化\大作业\数据处理\topCountry_gaofen.csv"
    people2_path = r"D:\个人\学习\大三下\数据可视化\大作业\数据处理\topCountry_difen.csv"
    csv_file = open(new_path, 'a+', newline='')
    csv_writer = csv.writer(csv_file)

    dfmovie=pd.read_csv(people2_path,encoding='gbk',header=None,error_bad_lines=False)
    count=0;
    # for chunk_movie in dfmovie


    newUK=['France']
    newF=['France']
    newC=['China']
    # print(newline)
    lines_movie = dfmovie.values.tolist()
    Alls=0
    ukAlls = 0
    fAlls = 0
    cAlls = 0
    Allp = 0
    ukAllp = 0
    fAllp = 0
    cAllp = 0

    for i in range(len(lines_movie)):
        count = count + 1
        newUSA = ['France']
        mid = lines_movie[i][0]
        print("现在开始读取第 {} 条电影id {} 信息".format(count, mid))
        P = []
        S = []
        Allp = 0;
        for j in range(5, 53, 2):#每年
            alls = 0
            Allp = Allp + lines_movie[i][j + 1]
            # print(j)
            for k in range(5, j + 2, 2):
                alls = alls + lines_movie[i][k] * lines_movie[i][k + 1]
            if(Allp!=0):
                ave = alls / Allp
            else:
                ave=0
            P.append(Allp)
            S.append(ave)
        P.append(lines_movie[i][56])
        S.append(lines_movie[i][55])
        if lines_movie[i][3] == 'France':
            newUSA.append(mid)
            newUSA.extend(S)
            newUSA.extend(P)
            print(newUSA)
            csv_writer.writerow(newUSA)
    csv_file.close()
    print("over")