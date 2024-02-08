import requests
from lxml import html
import winsound, time, webbrowser
frequency = 2500 
duration = 1000

url = 'http://www.ksef.or.kr/pc/notice/notice01.php'
res = requests.get(url)

tree = html.fromstring(res.content)
title = tree.xpath('//*[@id="bbs"]/div[2]/table/tbody/tr[1]/td[2]/a')
ind = 0

while True:
  res = requests.get(url)
  tree = html.fromstring(res.content)
  title = tree.xpath('//*[@id="bbs"]/div[2]/table/tbody/tr[1]/td[2]/a')

  if title[0].text != "[2023 KSEF 발표시간표 안내]":
    print("time: ", time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
    print("title: ", title[0].text)
    winsound.Beep(frequency, duration)
    webbrowser.open_new('http://www.ksef.or.kr/pc/notice/notice01.php')
    break

  else:
    print(ind, "iteration")
    ind+=1
    time.sleep(20)
    