# encoding: utf-8

import sys

reload(sys)
sys.setdefaultencoding('utf-8')

import requests
import re
import os
import json
from bs4 import BeautifulSoup
import glob
from snownlp import SnowNLP
from pyecharts import Bar


def get_joker_album_info(art_id):
    """
    得到专辑信息
    :param art_id:
    :return:
    """
    urls = "http://music.163.com/artist/album?id={}&limit=100&offset=0".format(art_id)
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Cookie': '_iuqxldmzr_=32; _ntes_nnid=dc7dbed33626ab3af002944fabe23bc4,1524151830800; _ntes_nuid=dc7dbed33626ab3af002944fabe23bc4; __utmc=94650624; __utmz=94650624.1524151831.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utma=94650624.1505452853.1524151831.1524151831.1524176140.2; WM_TID=RpKJQQ90pzUSYfuSWgFDY6QEK1Gb4Ulg; JSESSIONID-WYYY=ZBmSOShrk4UKH5K%5CVasEPuc0b%2Fq6m5eAE91jWCmD6UpdB2y4vbeazO%2FpQK%5CgiBW0MUDDWfB1EuNaV5c4wIJZ08hYQKDhpsHnDeMAgoz98dt%2B%2BFfhdiiNJw9Y9vRR5S4GU%2FziFp%2BliFX1QTJj%2BbaIGD3YxVzgumklAwJ0uBe%2FcGT6VeQW%3A1524179765762; __utmb=94650624.24.10.1524176140',
        'Host': 'music.163.com',
        'Referer': 'https://music.163.com/',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
    }
    html = requests.get(urls, headers=headers)
    pattern = re.compile(r'<div class="u-cover u-cover-alb3" title=(.*?)>')
    items = re.findall(pattern, html.text)
    cal = 0
    # 首先删除这个没文件，要不然每次都是追加
    if (os.path.exists("./txt/专辑信息.txt")):
        os.remove("专辑信息.txt")

    # 删除文件避免每次都要重复写入
    if (os.path.exists("./txt/专辑歌曲信息.txt")):
        os.remove("专辑歌曲信息.txt")

    for i in items:
        cal += 1
        # 这里需要注意i是有双引号的，所以需要注意转换下
        p = i.replace('"', '')
        # 这里在匹配里面使用了字符串，注意下
        pattern1 = re.compile(r'<a href="/album\?id=(.*?)" class="tit s-fc0">%s</a>' % (p))
        id1 = re.findall(pattern1, html.text)
        with open("./txt/专辑信息.txt", 'a') as f:
            f.write(u'专辑的名字是:{}!!专辑的ID是{} \n'.format(i, id1))
            GetLyric1(i, id1[0])
            f.close()

    print("总数是%d" % (cal))
    print("获取专辑以及专辑ID成功！！！！！")


def GetLyric1(album, id1):
    urls3 = "http://music.163.com/#/album?id={}".format(id1)
    print(urls3)
    # 将不要需要的符号去掉
    urls = urls3.replace("[", "").replace("]", "").replace("'", "").replace("#/", "")
    headers = {
        'Cookie': '_iuqxldmzr_=32; _ntes_nnid=dc7dbed33626ab3af002944fabe23bc4,1524151830800; _ntes_nuid=dc7dbed33626ab3af002944fabe23bc4; __utmz=94650624.1524151831.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utma=94650624.1505452853.1524151831.1524176140.1524296365.3; __utmc=94650624; WM_TID=RpKJQQ90pzUSYfuSWgFDY6QEK1Gb4Ulg; JSESSIONID-WYYY=7t6F3r9Uzy8uEXHPnVnWTXRP%5CSXg9U3%5CN8V5AROB6BIe%2B4ie5ch%2FPY8fc0WV%2BIA2ya%5CyY5HUBc6Pzh0D5cgpb6fUbRKMzMA%2BmIzzBcxPcEJE5voa%2FHA8H7TWUzvaIt%2FZnA%5CjVghKzoQXNM0bcm%2FBHkGwaOHAadGDnthIqngoYQsNKQQj%3A1524299905306; __utmb=94650624.21.10.1524296365',
        'Host': 'music.163.com',
        'Referer': 'http://music.163.com/',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36'
    }

    html = requests.get(urls, headers=headers)
    soup = BeautifulSoup(html.text, "html.parser")
    book_div = soup.find_all("ul")
    string_array = book_div[0].find_all("li")
    for something in string_array:
        html_data2 = something.find("a").text
        items = re.findall(r"\d+\.?\d*", str(something))
        with open("薛之谦专辑歌曲信息.txt", 'a') as f:
            print(len(something))
            if (len(something) > 0):
                f.write(u'薛之谦歌曲的名字是:{}!!歌曲的ID是{}\n'.format(html_data2, items))
                f.close()


def GetLyric2():
    # 首先删除原来的文件，避免重复写入
    for i in glob.glob("*热评*"):
        os.remove(i)
    for i in glob.glob("*歌曲名*"):
        os.remove(i)
    # 直接读取所有内容
    file_object = open('薛之谦专辑歌曲信息.txt'.decode('utf-8'), 'r+')
    list_of_line = file_object.readlines()

    namelist = ""

    for i in list_of_line:
        # 歌曲的名字是: 同一种调调!!歌曲的ID是['186020']
        pattern1 = re.compile(r'歌曲的名字是:(.*?)!!歌曲的ID是')
        pattern2 = re.compile(r'歌曲的ID是\[(.*?)\]')

        items1 = str(re.findall(pattern1, i)).replace("[", "").replace("]", "").replace("'", "")
        items2 = str(re.findall(pattern2, i)).replace("[", "").replace("]", "").replace('"', "").replace("'", "")

        headers = {
            'Request URL': 'http://music.163.com/weapi/song/lyric?csrf_token=',
            'Request Method': 'POST',
            'Status Code': '200 OK',
            'Remote Address': '59.111.160.195:80',
            'Referrer Policy': 'no-referrer-when-downgrade'
        }
        urls = "http://music.163.com/api/song/lyric?" + "id=" + str(items2) + '&lv=1&kv=1&tv=-1'
        html = requests.get(urls, headers=headers)
        json_obj = html.text
        j = json.loads(json_obj)
        try:
            lrc = j['lrc']['lyric']
            pat = re.compile(r'\[.*\]')
            lrc = re.sub(pat, "", lrc)
            lrc = lrc.strip()
            lrc = str(lrc)
            print("歌曲名-{}.txt".format(str(items1).decode('string_escape')))
            with open("歌曲名-{}.txt".format(str(items1).decode('string_escape')), 'a') as f:
                f.write(lrc)
                f.close()
            namelist = namelist + str(items1).decode('string_escape') + ".txt" + ","
            # 调用获取评论方法，并且把热评写入文件
            GetCmmons(str(items1).decode('string_escape'), items2)

        except:
            print("歌曲有错误 %s !!" % (items1))


def GetCmmons(song_name, id):
    """
    得到歌曲的评论
    :param song_name:
    :param id:
    :return:
    """
    # 删除原来的文件 避免重复爬取
    urls = "http://music.163.com/api/v1/resource/comments/R_SO_4_" + str(id)
    print(urls)
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Cookie': '_iuqxldmzr_=32; _ntes_nnid=dc7dbed33626ab3af002944fabe23bc4,1524151830800; _ntes_nuid=dc7dbed33626ab3af002944fabe23bc4; __utmz=94650624.1524151831.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); WM_TID=RpKJQQ90pzUSYfuSWgFDY6QEK1Gb4Ulg; JSESSIONID-WYYY=BgqSWBti98RpkHddEBZcxnxMIt4IdbCqXGc0SSxKwvRYlqbXDAApbgN%2FQWQ8vScdXfqw7adi2eFbe30tMZ13mIv9XOAv8bhrQYC6KRajksuYWVvTbv%2BOu5oCypc4ylh2Dk5R4TqHgRjjZgqFbaOF73cJlSck3lxcFot9jDmE9KWnF%2BCk%3A1524380724119; __utma=94650624.1505452853.1524151831.1524323163.1524378924.5; __utmc=94650624; __utmb=94650624.8.10.1524378924',
        'Host': 'music.163.com',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36'
    }

    html = requests.get(urls, headers=headers)
    html.encoding = 'utf8'
    json_obj = html.text
    j = json.loads(json_obj)
    i = j['hotComments']

    for uu in i:
        username = uu["user"]['nickname']
        likedCount1 = str(uu['likedCount'])
        comments = uu['content']
        with open(song_name + "专辑歌曲信息.txt", 'a') as f:
            f.write("用户名是 " + username + "\n")
            f.write("用户的评论是 " + comments + "\n")
            f.write("被点赞的次数是  " + str(likedCount1) + "\n")
            f.write("----------华丽的的分割线-------------" + "\n")
            f.close()


def MergedFile():
    """
    进行合文件操作
    :return:
    """
    aaa = 0
    for song_file_name in glob.glob("*歌曲名*"):
        file_object = open(song_file_name, 'r', )
        list_of_line = file_object.readlines()
        for p in list_of_line:
            if "作词" in p or "作曲" in p or "混音助理" in p or "混音师" in p or "录音师" in p or "执行制作" in p or "编曲" in p or "制作人" in p or "录音工程" in p or "录音室" in p or "混音录音室" in p or "混音工程" in p or "Programmer" in p or p == "\n" or "和声" in p or "吉他" in p or "录音助理" in p or "陈任佑鼓" in p or "薛之谦" in p:
                aaa += 1
            else:
                with open("allLyric" + ".txt", "a") as f:
                    f.write(p)
                    f.write("\n")
    file1 = open('allLyric.txt', 'r')  # 要去掉空行的文件
    file2 = open('allLyric_analysis.txt', 'w')  # 生成没有空行的文件

    try:
        for line in file1.readlines():
            if line == '\n':
                line = line.strip("\n")
            file2.write(line)
    finally:
        file1.close()
        file2.close()


def EmotionAnalysis():
    xzhou = []
    yzhou = []
    for i in glob.glob("*歌曲名*"):
        count = 0
        allsen = 0
        with open(i, 'r') as fileHandel:
            fileList = fileHandel.readlines()
            for p in fileList:
                if "作词" in p or "作曲" in p or "鼓" in p or "混音师" in p or "录音师" in p or "执行制作" in p or "编曲" in p or "制作人" in p or "录音工程" in p or "录音室" in p or "混音录音室" in p or "混音工程" in p or "Programmer" in p or p == "\n":
                    pass
                else:
                    s = SnowNLP(p)
                    s1 = SnowNLP(s.sentences[0])
                    # print(type(s1))
                    count += 1
                    allsen += s1.sentiments
        i = str(i)
        xzhou1 = i.split("-", 1)[1].split(".", 1)[0]
        xzhou.append(xzhou1)
        avg = allsen / count
        yzhou.append(avg)
        print("%s这首歌的情绪为%s" % (i, avg))
        fileHandel.close()

    bar = Bar("柱状图数据堆叠示例")
    bar.add("薛之谦歌曲情绪可视化", xzhou, yzhou, is_stack=True, xaxis_interval=0, xzhou1_label_textsize=0)
    bar.render(r"/Users/hengyuan/Desktop/api/fe/html/薛之谦歌曲情绪全部.html")
    # 显示最好的前五首歌
    import heapq
    yzhou1 = heapq.nlargest(10, yzhou)
    temp = map(yzhou.index, heapq.nlargest(10, yzhou))
    temp = list(temp)
    xzhou1 = []
    for i in temp:
        xzhou1.append(xzhou[i])
    # 情绪前十首歌个图
    bar = Bar("薛之谦歌曲情绪较好前十首歌")
    bar.add("薛之谦歌曲情绪可视化", xzhou1, yzhou1, is_stack=True)
    bar.render(r"/Users/hengyuan/Desktop/api/fe/html/薛之谦歌曲最积极情绪top10.html")
    # 显示最差的十首歌
    yzhou1 = heapq.nsmallest(10, yzhou)
    temp = map(yzhou.index, heapq.nsmallest(10, yzhou))
    temp = list(temp)
    xzhou1 = []
    for i in temp:
        xzhou1.append(xzhou[i])
    # print(xzhou1)
    # print(yzhou1)
    # 情绪前十首歌个图
    bar = Bar("薛之谦歌曲情绪较差前十首歌")
    bar.add("薛之谦歌曲情绪可视化", xzhou1, yzhou1, xaxis_interval=0, xzhou1_label_textsize=6)
    bar.render(r"/Users/hengyuan/Desktop/api/fe/html/薛之谦歌曲最消极情绪top10.html")


def splitSentence(inputFile, outputFile):
    import jieba.analyse
    fin = open(inputFile, 'r')
    fout = open(outputFile, 'w')
    for line in fin:
        line = line.strip()
        line = jieba.analyse.extract_tags(line)
        outstr = " ".join(line)
        fout.write(outstr + '\n')
    fin.close()
    fout.close()
    # 下面的程序完成分析前十的数据出现的次数
    f = open("分词过滤后.txt", 'r')
    a = f.read().split()
    info_data = sorted([(x, a.count(x)) for x in set(a)], key=lambda x: x[1], reverse=True)

    for write_data in info_data:
        with open("word.txt", 'a') as f:
            f.write(u'{}\n'.format(write_data[0]))
            f.close()


def LyricAnalysis():
    file = 'allLyric_analysis.txt'
    # 这个技巧需要注意
    alllyric = str([line.strip() for line in open('allLyric_analysis.txt').readlines()])
    # 获取全部歌词，在一行里面
    alllyric1 = alllyric.replace("'", "").replace(" ", "").replace("?", "").replace(",", "").replace('"', '').replace(
        "?", "").replace(".", "").replace("!", "").replace(":", "")

    # 在这里用结巴分词来分词过滤并且输出到一个文件里面，这个ting.txt
    import jieba.analyse  # 这里必须引入
    jieba.analyse.set_stop_words("ting.txt")
    splitSentence('allLyric_analysis.txt', '分词过滤后.txt')
    # 下面是词频统计
    import collections
    # 读取文本文件，把所有的汉字拆成一个list
    f = open("分词过滤后.txt", 'r')  # 打开文件，并读取要处理的大段文字
    txt1 = f.read()
    txt1 = txt1.replace('\n', '')  # 删掉换行符
    txt1 = txt1.replace(' ', '')  # 删掉换行符
    txt1 = txt1.replace('.', '')  # 删掉逗号
    txt1 = txt1.replace('.', '')  # 删掉句号
    txt1 = txt1.replace('o', '')  # 删掉句号
    mylist = list(txt1)
    mycount = collections.Counter(mylist)
    for key, val in mycount.most_common(10):  # 有序（返回前10个）
        print(key, val)
        # print(str(key).decode('string_escape'), val)


def sort_serialize(data):
    '''对数据字典进行排序'''
    try:
        return json.dumps(data, sort_keys=True, indent=4, ensure_ascii=False)
    except Exception as e:
        # print e
        return None


def wcdb():
    a = 5
    b = ++a
    print(b)


if __name__ == '__main__':
    # 薛之谦的专辑ID是 5781
    get_joker_album_info(5781)  # 得到专辑相关东西
    # 根据专辑返回的东西  爬到相关歌曲和信息
    # GetLyric2()
    # MergedFile()  # 合并文件，进行分析操作
    # EmotionAnalysis()

    # LyricAnalysis()
    # splitSentence('allLyric_analysis.txt', '分词过滤后.txt')
    # 单独测试一个歌曲
    # GetCmmons('dw', 553543014)
    # GetLyric1(38388012)
    # wordCloud.show_Joker_pic()
