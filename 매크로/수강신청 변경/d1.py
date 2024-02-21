from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import time 

driver = webdriver.Chrome()
driver.get('https://www.minjok.hs.kr/members/creg_reg_update_2022.php?code=D1&year=2024&term=1&grade=3&cflag=b&sflag=TjJRZGpqeWF3QmIvc2txY25xb1BCdz09')


# 학생 정보 입력
driver.find_element(By.XPATH, '/html/body/div/div[2]/table/tbody/tr[2]/td[2]/form/table/tbody/tr[1]/td[2]/input').send_keys('jhan756k')
driver.find_element(By.XPATH, '/html/body/div/div[2]/table/tbody/tr[2]/td[2]/form/table/tbody/tr[2]/td[2]/input').send_keys('060810')

# 학생 정보 입력 후 로그인 버튼 클릭
driver.find_element(By.XPATH, '/html/body/div/div[2]/table/tbody/tr[2]/td[2]/form/table/tbody/tr[1]/td[3]/input').click()

while True:
  driver.get('https://www.minjok.hs.kr/members/creg_reg_update_2022.php?code=D1&year=2024&term=1&grade=3&cflag=b&sflag=TjJRZGpqeWF3QmIvc2txY25xb1BCdz09')

  x = WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.XPATH, '/html/body/form/table[3]/tbody/tr[4]/td[1]/font/strong')))

  if x.text != r"◀ 정원마감":
    driver.find_element(By.XPATH, '/html/body/form/table[3]/tbody/tr[4]/td[1]/input').click()
    driver.find_element(By.XPATH, '/html/body/form/div/input[1]').click()
    WebDriverWait(driver, 10).until(EC.alert_is_present())
    driver.switch_to.alert.accept()
    break

  time.sleep(0.2)

driver.quit()