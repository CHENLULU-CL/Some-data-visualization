import csv
import pandas as pd

if __name__ == "__main__":
    new_path=r"D:\个人\学习\大三下\数据可视化\大作业\数据处理\types_gaofen_g.csv"

    people_path = r"D:\个人\学习\大三下\数据可视化\大作业\数据处理\topCountry_gaofen.csv"
    people2_path = r"D:\个人\学习\大三下\数据可视化\大作业\数据处理\topCountry_difen.csv"
    csv_file = open(new_path, 'a+', newline='')
    csv_writer = csv.writer(csv_file)

    dfmovie=pd.read_csv(people_path,encoding='gbk',header=None,error_bad_lines=False)
    count=0;
    # for chunk_movie in dfmovie:
    lines_movie = dfmovie.values.tolist()
    for i in range(len(lines_movie)):
        count = count + 1
        mid = lines_movie[i][0]
        print("现在开始读取第 {} 条电影id {} 信息".format(count, mid))

        newline =[mid,lines_movie[i][3]]
        types = lines_movie[i][4]
        T = types.split("|")
        newline.extend(T)
        print(newline)
        csv_writer.writerow(newline)
    csv_file.close()
    print("over")