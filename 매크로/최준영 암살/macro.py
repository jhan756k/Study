from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

optionsc = Options()
optionsc.add_argument("--disable-extensions")
optionsc.add_argument(r"user-data-dir=C:\Users\jhan7\AppData\Local\Google\Chrome\User Data")
optionsc.add_argument("--headless")
refreshrate = 0.2

driver = webdriver.Chrome(options=optionsc) 
driver.get('https://kmlaonline.net/board/all_announce/view/499467')

while True:
    driver.refresh()
    time.sleep(refreshrate)