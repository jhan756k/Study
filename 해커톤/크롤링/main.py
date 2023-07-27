from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

baseUrl = r"https://sanjaecase.comwel.or.kr/service/dataView?id="
nameUrl = r"https://sanjaecase.comwel.or.kr/service/dataListReverse?gubun2=%EC%9E%91%EC%97%85%EC%8B%9C%EA%B0%84%EC%A4%91%EC%82%AC%EA%B3%A0&gubun=&pageUnit=200&pageIndex="

driver = webdriver.Chrome()

for i in range(46):
    driver.get(nameUrl + str(i+1))
    driver.maximize_window()
    WebDriverWait(driver, 30).until(EC.presence_of_element_located(
            (By.XPATH, f'/html/body/div/div[2]/div[2]/div/div[3]/div[2]/div[1]/table/tbody')))
    
    for j in range(200): 
        casenum = i * 200 + j + 1
        casename = driver.find_element(By.XPATH, f"/html/body/div/div[2]/div[2]/div/div[3]/div[2]/div[1]/table/tbody/tr[{j+1}]/td[3]/a/span").text[1:-1]
        casename+="_"
        casename +=driver.find_element(By.XPATH, f"/html/body/div/div[2]/div[2]/div/div[3]/div[2]/div[1]/table/tbody/tr[{j+1}]/td[3]/a").text.split("\n")[0]
        print(casenum, casename)


