from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
import time
import datetime

def today_date():
    datetime.datetime.today()
    datetime.datetime(2012, 3, 23, 23, 24, 55, 173504)
    return datetime.datetime.today().weekday()


misulurl = '/html/body/div/div[2]/div[1]/div[2]/div[2]/div/dl[2]/dd/ul/li[1]/a/i'
suhakurl = '/html/body/div/div[2]/div[1]/div[2]/div[2]/div/dl[2]/dd/ul/li[2]/a/i'
gwahakurl = '/html/body/div/div[2]/div[1]/div[2]/div[2]/div/dl[2]/dd/ul/li[3]/a/i'
yuksaurl = '/html/body/div/div[2]/div[1]/div[2]/div[2]/div/dl[2]/dd/ul/li[4]/a/i'
youngwhaurl = '/html/body/div/div[2]/div[1]/div[2]/div[2]/div/dl[2]/dd/ul/li[5]/a/i'
englishurl = '/html/body/div/div[2]/div[1]/div[2]/div[2]/div/dl[2]/dd/ul/li[6]/a/i'
dodukurl = '/html/body/div/div[2]/div[1]/div[2]/div[2]/div/dl[2]/dd/ul/li[7]/a/i'
gukuurl = '/html/body/div/div[2]/div[1]/div[2]/div[2]/div/dl[2]/dd/ul/li[8]/a/i'
cheyukurl = '/html/body/div/div[2]/div[1]/div[2]/div[2]/div/dl[2]/dd/ul/li[9]/a/i'
umakurl = '/html/body/div/div[2]/div[1]/div[2]/div[2]/div/dl[2]/dd/ul/li[10]/a/i'
soccerurl = '/html/body/div/div[2]/div[1]/div[2]/div[2]/div/dl[2]/dd/ul/li[11]/a/i'
hanmunurl = '/html/body/div/div[2]/div[1]/div[2]/div[2]/div/dl[2]/dd/ul/li[12]/a/i'
index = None

if today_date() == 0:
    driver = webdriver.Chrome()
    url = 'https://oc31.ebssw.kr/onlineClass/search/onlineClassSearchView.do?schulCcode=00898&schCssTyp=online_mid'
    driver.get(url)
    driver.maximize_window()
    action = ActionChains(driver)

    WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, ".my_menu>a"))).click()

    time.sleep(1)

    driver.find_element_by_xpath('//*[@id="header"]/div[1]/div/div/div/div/ul/li[1]/a').click()
    action.send_keys('jh756k').key_down(Keys.TAB).send_keys('supercube098').key_down(Keys.ENTER).perform()
    time.sleep(1)
    action.reset_actions()
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, ".my_menu>a"))).click()
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/div/header/div[1]/div/div/div/div/ul/li[1]/a').click()
    time.sleep(1)

    driver.find_element_by_xpath(dodukurl).click()
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(1)
    driver.get('https://oc31.ebssw.kr/onlineClass/reqst/onlineClassReqstInfoView.do')
    time.sleep(1)
    driver.find_element_by_xpath(gukuurl).click()
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[2])
    time.sleep(1)
    driver.get('https://oc31.ebssw.kr/onlineClass/reqst/onlineClassReqstInfoView.do')
    time.sleep(1)
    driver.find_element_by_xpath(yuksaurl).click()
    index = 3

elif today_date() == 1:
    driver = webdriver.Chrome()
    url = 'https://oc31.ebssw.kr/onlineClass/search/onlineClassSearchView.do?schulCcode=00898&schCssTyp=online_mid'
    driver.get(url)
    driver.maximize_window()
    action = ActionChains(driver)

    WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, ".my_menu>a"))).click()

    time.sleep(1)

    driver.find_element_by_xpath('//*[@id="header"]/div[1]/div/div/div/div/ul/li[1]/a').click()
    action.send_keys('jh756k').key_down(Keys.TAB).send_keys('supercube098').key_down(Keys.ENTER).perform()
    time.sleep(1)
    action.reset_actions()
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, ".my_menu>a"))).click()
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/div/header/div[1]/div/div/div/div/ul/li[1]/a').click()
    time.sleep(1)

    driver.find_element_by_xpath(gwahakurl).click()
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(1)
    driver.get('https://oc31.ebssw.kr/onlineClass/reqst/onlineClassReqstInfoView.do')
    time.sleep(1)
    driver.find_element_by_xpath(cheyukurl).click()
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[2])
    time.sleep(1)
    driver.get('https://oc31.ebssw.kr/onlineClass/reqst/onlineClassReqstInfoView.do')
    time.sleep(1)
    driver.find_element_by_xpath(dodukurl).click()
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[3])
    time.sleep(1)
    driver.get('https://oc31.ebssw.kr/onlineClass/reqst/onlineClassReqstInfoView.do')
    time.sleep(1)
    driver.find_element_by_xpath(soccerurl).click()
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[4])
    time.sleep(1)
    driver.get('https://oc31.ebssw.kr/onlineClass/reqst/onlineClassReqstInfoView.do')
    time.sleep(1)
    driver.find_element_by_xpath(englishurl).click()
    index = 5

elif today_date() == 2:
    driver = webdriver.Chrome()
    url = 'https://oc31.ebssw.kr/onlineClass/search/onlineClassSearchView.do?schulCcode=00898&schCssTyp=online_mid'
    driver.get(url)
    driver.maximize_window()
    action = ActionChains(driver)

    WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, ".my_menu>a"))).click()

    time.sleep(1)

    driver.find_element_by_xpath('//*[@id="header"]/div[1]/div/div/div/div/ul/li[1]/a').click()
    action.send_keys('jh756k').key_down(Keys.TAB).send_keys('supercube098').key_down(Keys.ENTER).perform()
    time.sleep(1)
    action.reset_actions()
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, ".my_menu>a"))).click()
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/div/header/div[1]/div/div/div/div/ul/li[1]/a').click()
    time.sleep(1)

    driver.find_element_by_xpath(englishurl).click()
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(1)
    driver.get('https://oc31.ebssw.kr/onlineClass/reqst/onlineClassReqstInfoView.do')
    time.sleep(1)
    driver.find_element_by_xpath(youngwhaurl).click()
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[2])
    time.sleep(1)
    driver.get('https://oc31.ebssw.kr/onlineClass/reqst/onlineClassReqstInfoView.do')
    time.sleep(1)
    driver.find_element_by_xpath(yuksaurl).click()
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[3])
    time.sleep(1)
    driver.get('https://oc31.ebssw.kr/onlineClass/reqst/onlineClassReqstInfoView.do')
    time.sleep(1)
    driver.find_element_by_xpath(suhakurl).click()
    index = 4

elif today_date() == 3:
    driver = webdriver.Chrome()
    url = 'https://oc31.ebssw.kr/onlineClass/search/onlineClassSearchView.do?schulCcode=00898&schCssTyp=online_mid'
    driver.get(url)
    driver.maximize_window()
    action = ActionChains(driver)

    WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, ".my_menu>a"))).click()

    time.sleep(1)

    driver.find_element_by_xpath('//*[@id="header"]/div[1]/div/div/div/div/ul/li[1]/a').click()
    action.send_keys('jh756k').key_down(Keys.TAB).send_keys('supercube098').key_down(Keys.ENTER).perform()
    time.sleep(1)
    action.reset_actions()
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, ".my_menu>a"))).click()
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/div/header/div[1]/div/div/div/div/ul/li[1]/a').click()
    time.sleep(1)

    driver.find_element_by_xpath(umakurl).click()
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(1)
    driver.get('https://oc31.ebssw.kr/onlineClass/reqst/onlineClassReqstInfoView.do')
    time.sleep(1)
    driver.find_element_by_xpath(hanmunurl).click()
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[2])
    time.sleep(1)
    driver.get('https://oc31.ebssw.kr/onlineClass/reqst/onlineClassReqstInfoView.do')
    time.sleep(1)
    driver.find_element_by_xpath(cheyukurl).click()
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[3])
    time.sleep(1)
    driver.get('https://oc31.ebssw.kr/onlineClass/reqst/onlineClassReqstInfoView.do')
    time.sleep(1)
    driver.find_element_by_xpath(gukuurl).click()
    index = 4

elif today_date() == 4:
    driver = webdriver.Chrome()
    url = 'https://oc31.ebssw.kr/onlineClass/search/onlineClassSearchView.do?schulCcode=00898&schCssTyp=online_mid'
    driver.get(url)
    driver.maximize_window()
    action = ActionChains(driver)

    WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, ".my_menu>a"))).click()

    time.sleep(1)

    driver.find_element_by_xpath('//*[@id="header"]/div[1]/div/div/div/div/ul/li[1]/a').click()
    action.send_keys('jh756k').key_down(Keys.TAB).send_keys('supercube098').key_down(Keys.ENTER).perform()
    time.sleep(1)
    action.reset_actions()
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, ".my_menu>a"))).click()
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/div/header/div[1]/div/div/div/div/ul/li[1]/a').click()
    time.sleep(1)

    driver.find_element_by_xpath(gwahakurl).click()
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(1)
    driver.get('https://oc31.ebssw.kr/onlineClass/reqst/onlineClassReqstInfoView.do')
    time.sleep(1)
    driver.find_element_by_xpath(suhakurl).click()
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[2])
    time.sleep(1)
    driver.get('https://oc31.ebssw.kr/onlineClass/reqst/onlineClassReqstInfoView.do')
    time.sleep(1)
    driver.find_element_by_xpath(misulurl).click()
    index = 3

else:
    print("No schools on Weekends YAAAYYYY!!!!!!")

# Open Band
url = 'https://band.us/en'
driver.execute_script("window.open('');")
driver.switch_to.window(driver.window_handles[index])
time.sleep(1)
driver.get(url)
driver.maximize_window()
action = ActionChains(driver)

driver.find_element_by_xpath('/html/body/div[1]/div/header/div/div/a[2]').click()
driver.find_element_by_xpath('/html/body/div/section/ul/li[2]/a').click()
action.send_keys("jhan756k@gmail.com").perform()
driver.find_element_by_xpath('/html/body/div/section/form/button/span').click()
action.reset_actions()
action = ActionChains(driver)
action.send_keys("supercube098").perform()
driver.find_element_by_xpath('/html/body/div/section/form/button').click()
driver.find_element_by_xpath('/html/body/div/section/form/div[1]/div/input').click()

