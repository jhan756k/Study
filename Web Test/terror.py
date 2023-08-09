import requests, random

url = "https://badada.gibal.net/result/"
cnt = 0

while True:
    data = {"answer":[1,2,3,4,random.randint(12, 15),6,7,random.randint(12,15),9,10,11,random.randint(12, 15)]}
    res = requests.post(url, json=data)
    cnt += 1
    if res.status_code == 500:
        exit()
    print(cnt)