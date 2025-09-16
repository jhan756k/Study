from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import re
import json

config_path = 'config.json'

with open(config_path, 'r') as f:
    config = json.load(f)

url = config['url']
username = config['id']
passkey = config['password']

refresh_interval = 1  # seconds

def setup_driver():
    options = webdriver.ChromeOptions()
    options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
    options.add_experimental_option("detach", True)
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)

    driver = webdriver.Chrome(options=options)
    return driver

driver = setup_driver()

driver.get(url)

id = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div[2]/div/fieldset/form/div/div[2]/input'))
)
password = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div[2]/div/fieldset/form/div/div[3]/input'))
)
loginbtn = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div[2]/div/fieldset/form/div/div[5]/button'))
)

id.send_keys(username)
password.send_keys(passkey)
loginbtn.click()

WebDriverWait(driver, 10).until(
    EC.frame_to_be_available_and_switch_to_it((By.ID, "ContentFrame"))
)

while True:

    find_course_btn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "btnSch"))
    ).click()

    time.sleep(refresh_interval)

    checkbtn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'checkAll'))
    )
    checkboxes = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.ID, 'divGrxMst'))
    )

    checkbtn.click()
    applybtn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'btnBatch'))
    ).click()

    alert = WebDriverWait(driver, 10).until(EC.alert_is_present())
    alerttext = alert.text
    alert.accept()
    first_line = alerttext.splitlines()[0]
    match = re.search(r'성공:(\d+)건\s*/\s*실패:(\d+)건', first_line)
    if match:
        success_num = int(match.group(1))
        failure_num = int(match.group(2))
    else:
        success_num = None
        failure_num = None
    print(f"Success: {success_num}, Failure: {failure_num}")
