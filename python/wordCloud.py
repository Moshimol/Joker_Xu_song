# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator, STOPWORDS
import jieba


def show_Joker_pic():
    # 读入背景图片
    backgroud_Image = plt.imread("./word_pic/way_pic.jpg")
    # 读取要生成词云的文件
    text_from_file_with_apath = open("word.txt").read()
    # 通过jieba分词进行分词并通过空格分隔
    wordlist_after_jieba = jieba.cut(text_from_file_with_apath, cut_all=True)
    wl_space_split = " ".join(wordlist_after_jieba)
    my_wordcloud = WordCloud(
        background_color='white',  # 设置背景颜色
        mask=backgroud_Image,  # 设置背景图片
        max_words=10000,  # 设置最大现实的字数
        stopwords=STOPWORDS,  # 设置停用词
        font_path='/Library/Fonts/Songti.ttc',  # 设置字体格式，如不设置显示不了中文 Mac是这样的设置方式
        max_font_size=50,  # 设置字体最大值
        random_state=300,  # 设置有多少种随机生成状态，即有多少种配色方案
        scale=10,
        width=16000,
        height=8000
    ).generate(wl_space_split)

    # 根据图片生成词云颜色
    image_colors = ImageColorGenerator(backgroud_Image)
    my_wordcloud.recolor(color_func=image_colors)
    # 以下代码显示图片
    plt.imshow(my_wordcloud)
    plt.axis("off")
    print 'over'
    plt.show()
    my_wordcloud.to_file('./word_pic/show_Chinese.png')

