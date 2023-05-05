import csv
from wordcloud import WordCloud, ImageColorGenerator  # 引入词云WordCloud
import matplotlib.pyplot as plt                       # 制图包， as作用是重命名长度大的程序，方便引用写码
from PIL import Image
import numpy as np                                      #科学数值计算包，可用来存储和处理大型矩阵

csv_file = open(r'E:\学习\大三下\数据可视化\pycharmprojects\词云\Dciping_China.csv', 'a+', newline='')
csv_writer = csv.writer(csv_file)


if __name__ == "__main__":

    word_dct = {}


    # 存放每年的标签及次数
    local_path = r"E:\学习\大三下\数据可视化\pycharmprojects\词云\types_difen_g_China.csv"
    with open(local_path) as fb:
        reader = csv.reader(fb)
        for row in reader:
            print(row[2])
            if row[2] in word_dct:
                word_dct[row[2]] += 1
            else:
                word_dct[row[2]] = 1

            if row[3] in word_dct:
                word_dct[row[3]] += 1
            else:
                word_dct[row[3]] = 1

            if row[4] in word_dct:
                word_dct[row[4]] += 1
            else:
                word_dct[row[4]] = 1

            if row[5] in word_dct:
                word_dct[row[5]] += 1
            else:
                word_dct[row[5]] = 1

            # if row[6] in word_dct:
            #     word_dct[row[6]] += 1
            # else:
            #     word_dct[row[6]] = 1
    del word_dct['']   # 删掉空字符串
    print(word_dct)

    # 词频排序,从大到小
    order = sorted(word_dct.items(), key=lambda item: item[1], reverse=True)
    print(order)
    # for dct in order:
    #     csv_writer.writerow([dct[0], dct[1]])

    # 绘制词云
    path_img = r"E:\学习\大三下\数据可视化\pycharmprojects\词云\USAmap.jpg"
    background_image = np.array(Image.open(path_img))

    wordcloud = WordCloud(
        background_color='white',  # 默认为图片背景为黑色，英文White表示输出的词云图片背景为白色。
        scale=15,  # 默认之为1。可以理解为生成的图片像素密度值，值越大，图片密度越高，越清楚。

        mask=background_image
        # font_path='c:\windows\Fonts\simhei.ttf',  # 写明地址，指定文字的类型为中文黑体。
    ).generate_from_frequencies(word_dct)

    # 运行成功后显示图片
    # plt.savefig(r'E:\学习\大三下\数据可视化\pycharmprojects\词云\1995-2019高分电影词云图\2019高分电影词云图.jpg', dpi=900)
    # plt.title("2019高分电影词云图")  # 标题
    plt.imshow(wordcloud,
               interpolation='bilinear')  # Bilinear：双线性插值算法，用来缩放显示图片。缩放就是把原图片的像素应用坐标系统，
                                    # 用坐标表示，双线性插值算法就是把一个坐标不是整数的点的坐标，用最近的四个整数点坐标指示出来；

    plt.axis('off')  # 不显示坐标尺度
    plt.show()

    csv_file.close()  # 关闭csv文件




