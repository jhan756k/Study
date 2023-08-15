import requests, random

url = "https://badada.gibal.net/result/"
cnt = 0

while True:
    data = {"answer":[1,2,3,4,5,6,7,8,9,10,11,37]}
    res = requests.post(url, json=data)
    cnt += 1
    if res.status_code == 500:
        exit()
    print(cnt)