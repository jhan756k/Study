import selenium
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import Select


url = "https://google.com"
driver = webdriver.Chrome()
driver.get(url) # Go to webpage
driver.maximize_window()

action = ActionChains(driver)
action.send_keys("guguassssss").perform()
action.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()