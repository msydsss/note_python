#ニュース取得
import requests
import datetime
from urllib.request import urlopen
from bs4 import BeautifulSoup

OAT = 4979
APAMAN = 8889
DNP = 7912
TOYO = 6330

oat = "OATアグリオ"
apaman = "APAMAN"
dnp = "大日本印刷"
toyo = "東洋エンジニアリング"


stock_list = [OAT,APAMAN,DNP,TOYO]
stock_name = [oat,apaman,dnp,toyo]

news_url = "https://kabutan.jp"

#企業概要
for (i,ii) in zip(stock_list,stock_name):
    list = []
    url = "https://kabutan.jp/stock/news?code=" + str(i) + "&nmode=1"
    html = urlopen(url)
    bs = BeautifulSoup(html, "html.parser")
    table = bs.findAll("table",{"class":"s_news_list"})
    today = datetime.datetime.today()
    yesterday = today - datetime.timedelta(days=1)
    threeday = yesterday - datetime.timedelta(days=1)

    today = str(today)[2:10].replace("-", "/")
    yesterday = str(yesterday)[2:10].replace("-", "/")
    threeday = str(threeday)[2:10].replace("-", "/")



    for count in table:
        print("★" + ii + "(" + str(i) + ")\n")
        for o in range(5):
            time = count.findAll("td",{"class":"news_time"})[o].get_text()[0:8]
            if today == time or yesterday == time or threeday == time:
                link = bs.findAll('tr')[7 + o].get_text()[16:]
                link_url = bs.findAll("a")[53+ 0]
                print("日付：" + time,link,news_url + link_url.get("href")+"\n")

            else:
                pass
        print("処理完了")
        print("------------------------------------------------------------------")
