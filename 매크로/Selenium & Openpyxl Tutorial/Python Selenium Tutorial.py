# Selenium basic imports
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

driver = webdriver.Chrome() # Defines Browser (YOU MUST HAVE THE BROWSER DRIVER INSTALLED IN THE SAME FILE PATH)
driver.get('https://www.office.com/launch/excel?ui=en-US&rs=US&auth=1') # Go to webpage
driver.maximize_window()
#assert "login" in driver.title       (Insures that there is str "office" in the browser title)
#assert "No results found." not in driver.page_source

username = ActionChains(driver) # Define an actionchain
username.send_keys("jhan756k@gmail.com").key_down(Keys.ENTER).perform()
username.reset_actions()

time.sleep(1)

password = ActionChains(driver)
password.send_keys("supercube098#").key_down(Keys.ENTER).perform()
password.reset_actions()

time.sleep(2)

driver.find_element_by_id('expandable-list-unpinned-mru').click()
driver.switch_to.window(driver.window_handles[0]) # Switches window
driver.close()
driver.switch_to.window(driver.window_handles[0])

# WEBDRIVERWAIT: Wait 5 seconds till element is located (By.ID, NAME, etc)
# If unable to find element in less than 5 seconds, print "Time out"

try:
    element_present = EC.presence_of_element_located((By.ID, 'element_id'))
    WebDriverWait(driver, 5).until(element_present)

except TimeoutException:
    print("Time out")

# SELECT CLASS

select = Select(driver.find_element_by_name('name'))  # Selects by attributes 
select.select_by_index(index)
select.select_by_visible_text("text")
select.select_by_value(value)
select.deselect_all() # deselects
all_selected_options = select.all_selected_options # Returns selected list
options = select.options # To get options
element.submit() # Automatically finds submit button; NoSuchElementException raised when there is none

# DRAG AND DROP

element = driver.find_element_by_name("source")
target = driver.find_element_by_name("target")

action_chains = ActionChains(driver)
action_chains.drag_and_drop(element, target).perform() # Drags Element to Target

alert = driver.switch_to_alert() # POPUP DIALOGS



