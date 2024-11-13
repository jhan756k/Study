from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time, random

msg = ["끝까지 포기하지 않고 달려가자!", "오늘의 노력이 내일의 꿈이 된다!", "네가 최선을 다한 만큼 결과도 따라올 거야!", "너라면 할 수 있어!", "너의 노력이 빛을 발할 거야!", "후회 없는 하루를 만들어 보자!", "내일의 자신을 위해 오늘도 힘내자!", "너의 가능성은 무한해!", "마지막까지 최선을 다해!", "할 수 있어, 네가 준비한 모든 걸 보여줘!", "성공은 노력하는 자의 몫이다!", "네가 흘린 땀방울이 빛날 순간이야!", "지금 이 순간이 곧 소중한 추억이 될 거야!", "모든 순간이 너에게 중요한 의미가 될 거야!", "너의 노력은 결코 헛되지 않아!", "믿고 나아가자, 넌 준비됐어!", "시험장에서 너의 빛나는 순간을 만들어!", "끝까지 최선을 다하는 네가 자랑스러워!", "너의 꿈을 이루는 그날까지 힘내자!", "후회 없는 하루를 위해 오늘도 파이팅!", "네가 목표한 바를 향해 나아가자!", "절대 포기하지 말고 끝까지 파이팅!", "내일을 위한 오늘의 노력이 너를 빛나게 할 거야!", "모든 순간이 네 노력의 증거야!", "너의 실력과 노력을 믿어!", "지금 이 순간을 위해 준비해 온 너야!", "너의 길에 밝은 빛이 될 오늘을 만들어보자!", "노력하는 너의 모습이 아름다워!", "너의 꿈을 이루기 위해 달려가자!", "할 수 있어, 너라면 충분히 가능해!", "힘든 순간일수록 넌 더 강해질 거야!", "너의 꿈을 위해 오늘도 최선을 다하자!", "열정과 노력을 믿어!", "너의 빛나는 미래를 위해 달려가자!", "너의 도전이 아름답다!", "오늘 하루는 네 인생에 큰 의미가 될 거야!", "네 자신을 믿어, 넌 충분히 해낼 수 있어!", "자신감을 가지고 도전하자!", "네가 지금까지 쌓아온 실력을 보여줘!", "수많은 노력의 결실을 맺을 시간!", "마지막까지 너의 힘을 다하자!", "너의 목표를 위해 파이팅!", "너의 잠재력은 그 누구도 모를 거야!", "너의 열정이 빛날 순간이야!", "모든 준비가 완벽하니 자신감을 가져!", "오늘이 너의 인생에 특별한 하루가 될 거야!", "끝까지 집중하고 네 모든 걸 보여줘!", "네가 흘린 땀방울이 보상을 받을 순간이야!", "네가 걸어온 길이 빛날 거야!", "포기하지 않고 달려온 너, 대견해!", "너의 열정이 불타오를 시간이야!", "자신을 믿고 앞으로 나아가자!", "오늘을 위해 준비해 온 모든 것을 보여줘!", "네 노력은 절대 배신하지 않아!", "너의 잠재력은 무한해!", "모든 순간이 너의 꿈을 위한 과정이야!", "오늘도 파이팅! 너의 꿈은 가까워!", "최고의 결과를 향해 달려가자!", "너의 열정이 승리할 거야!", "모든 준비가 완벽하니 파이팅!", "너의 미래가 빛날 시간이야!", "마지막까지 너의 꿈을 향해 달려가자!", "너의 가능성을 믿어!", "너의 노력이 결실을 맺을 순간이야!", "포기하지 말고 끝까지 달려가자!", "모든 순간이 너의 노력의 증거야!", "네가 흘린 땀이 빛날 거야!", "할 수 있어, 네가 준비한 모든 걸 보여줘!", "최선을 다하는 네 모습이 아름다워!", "오늘의 노력이 내일의 너를 만들 거야!", "네가 원하는 결과가 올 거야!", "모든 순간이 너의 꿈을 위한 과정이야!", "너의 노력이 결실을 맺는 날!", "너의 가능성은 무한하니까!", "끝까지 포기하지 말자!", "너의 열정이 너를 빛나게 할 거야!", "마지막까지 최선을 다해!", "할 수 있어, 네가 원하는 미래가 바로 여기 있어!", "너의 꿈을 위해 오늘도 최선을 다하자!", "끝까지 포기하지 않고 달려가자!", "모든 순간이 너의 노력을 증명할 거야!", "오늘도 네 꿈을 위해 파이팅!", "너의 노력이 반드시 결실을 맺을 거야!", "끝까지 최선을 다해, 넌 해낼 수 있어!", "너의 꿈을 위해 최선을 다하자!", "오늘도 너의 목표를 위해 달려가자!", "할 수 있어, 네가 원하는 미래가 가까워!", "네 자신을 믿고 도전하자!", "네가 원하는 결과가 반드시 올 거야!", "너의 꿈을 위해 오늘도 파이팅!", "오늘이 네 인생에 중요한 날이 될 거야!", "끝까지 포기하지 않고 달려가자!"]

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches",["ignore-certificate-errors"])
options.add_argument('headless')
driver = webdriver.Chrome(options=options)
driver.get("https://www.ferrerorocher.com/kr/ko/xp/ferrero-golden-cheer/card_info.asp")
driver.maximize_window()
driver.execute_script("document.body.style.zoom='50%'")

t = 100

for _ in range(t):
  driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/form/input[3]').send_keys('민족사관')
  driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/form/button').click()
  WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div/div/div/div/div[2]/table/tbody/tr/td[1]/a'))).click()
  WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/div[4]/button'))).click()
  WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div/div/div[1]'))).send_keys(msg[random.randrange(0, len(msg))])
  WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div/div/button'))).click()
  driver.get("https://www.ferrerorocher.com/kr/ko/xp/ferrero-golden-cheer/card_info.asp")
  print(_+1, "th complete!")
  time.sleep(random.randrange(0, 4))
  
driver.quit()