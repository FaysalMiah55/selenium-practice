from selenium import webdriver
import time
from selenium.webdriver.common.by import By 
import re
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.action_chains import ActionChains

chrome_options = Options()
chrome_options.add_argument("--disable-cache")
chrome_options.add_argument("--incognito")
driver = webdriver.Chrome(options=chrome_options)
# driver = webdriver.Chrome()



driver.get('https://www.google.com/')

driver.maximize_window()

search_box = driver.find_element(By.NAME, "q")

search_box.send_keys("Laptop Shop Near Mirpur")

search_box.send_keys(Keys.RETURN)

# time.sleep(200)


time.sleep(1000)
driver.quit()