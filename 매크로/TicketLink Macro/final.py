from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
import json

game_name = "인천vs수원"
game_link = "https://www.ticketlink.co.kr/sports/138/77"
seat_type = "원정"
open_time = "2025-02-25 13:59:59"
areaname = ["N-4", "N4"]
seat_num = 2

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

driver.get(game_link)

with open("cookies.json", "r") as file:
    cookies = json.load(file)
    for cookie in cookies:
        cookie.pop("domain", None)
        try:
            driver.add_cookie(cookie)
        except Exception as e:
            print(f"Failed to add cookie: {cookie}\nError: {e}")
driver.refresh()

target_time = time.mktime(time.strptime(open_time, "%Y-%m-%d %H:%M:%S")) + 0.8

while True:
    current_time = time.time()
    if current_time >= target_time:
        driver.refresh()

        while True:
            try:
                if "예매하기" in WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located(
                        (By.CLASS_NAME, "match_btn"))
                ).text:
                    break
                else:
                    driver.refresh()
            except Exception as e:
                print(f"Error while checking for ticket button: {e}")
                break
        break

    time.sleep(0.001)

reserve_list = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "reserve_lst_bx"))
)
list_items = reserve_list.find_elements(By.TAG_NAME, "li")

for li in list_items:
    match_team_info = li.find_element(By.CLASS_NAME, "match_team_info")
    if game_name in match_team_info.text:
        match_btn = li.find_element(By.CLASS_NAME, "match_btn")
        ActionChains(driver).move_to_element(match_btn).click().perform()
        break

WebDriverWait(driver, 10).until(lambda d: len(d.window_handles) > 1)
driver.switch_to.window(driver.window_handles[1])

seat_grade_list = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "select_seat_grade"))
)
seat_items = seat_grade_list.find_elements(By.TAG_NAME, "li")

for item in seat_items:
    if seat_type in item.text:
        item.click()
        break

seat_grade_list = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "select_seat_grade"))
)
seat_items = seat_grade_list.find_elements(By.TAG_NAME, "li")

for item in seat_items:
    if seat_type in item.text:
        area = item.find_element(By.TAG_NAME, "ul")
        area_items = area.find_elements(By.TAG_NAME, "li")
        for ai in area_items:
            if areaname[0] in ai.text or areaname[1] in ai.text:
                ai.click()
                break
        break
