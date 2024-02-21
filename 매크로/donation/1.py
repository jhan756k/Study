from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import time
from datetime import datetime

driver = webdriver.Chrome()
driver.get("https://kmlaonline.net/")

driver.find_element(By.XPATH, '/html/body/div[7]/div[4]/div/div[2]/form/div/div[1]/div[1]/input').send_keys('jhan756k')
driver.find_element(By.XPATH, '/html/body/div[7]/div[4]/div/div[2]/form/div/div[1]/div[2]/input').send_keys('supercube098')
driver.find_element(By.XPATH, '/html/body/div[7]/div[4]/div/div[2]/form/div/div[1]/div[3]/button').click()
driver.get("https://kmlaonline.net/util/donation-book")

def about_time():
  now = datetime.now()
  current_time = now.strftime("%H%M%S")
  if int(current_time) >= 185957:
    return True
  else:
    return False
  
def check_xpath(xpath):
  if driver.find_elements(By.XPATH, xpath):
    return True
  else:
    return False
  
test = '/html/body/div[7]/div[4]/div/div[2]/table[2]/tbody/tr[83]/td[3]/form/input[5]'
englang = '/html/body/div[7]/div[4]/div/div[2]/table[2]/tbody/tr[6]/td[3]/form/input[5]'
dsat = '/html/body/div[7]/div[4]/div/div[2]/table[2]/tbody/tr[30]/td[3]/form/input[5]'
arduino = '/html/body/div[7]/div[4]/div/div[2]/table[3]/tbody/tr[70]/td[3]/form/input[5]'
toner = '/html/body/div[7]/div[4]/div/div[2]/table[5]/tbody/tr[233]/td[4]/form/input[5]'

while True:
  if not about_time():
    time.sleep(1)
    continue
  else:
    break

while True:
  
  driver.get("https://kmlaonline.net/util/donation-book")

  if not check_xpath(test):
    continue

  else:
    driver.find_element(By.XPATH, englang).click()
    break
  