from selenium import webdriver
import json, time
driver = webdriver.Chrome()

driver.get("https://www.ticketlink.co.kr/sports/138/77")
time.sleep(30)

cookies = driver.get_cookies()
with open("cookies.json", "w") as file:
    json.dump(cookies, file)

driver.quit()
