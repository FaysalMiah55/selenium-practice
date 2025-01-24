import time
from selenium import webdriver
from selenium.webdriver.common.by import By

##chrome_driver
# from selenium.webdriver.chrome.service import Service
# service_obj = Service("Users/prime/Downloads/chromedriver")
# driver = webdriver.Chrome(service=service_obj)

driver = webdriver.Chrome()
driver.get("https://innovativeskillsbd.com/signup")

driver.find_element(By.NAME, "name").send_keys("Prime")
driver.find_element(By.ID, "email").send_keys("prime@gmail.com")
driver.find_element(By.ID, "phone").send_keys("01700000000")
driver.find_element(By.XPATH, '//*[@id="pass"]').send_keys("123456")

driver.maximize_window()
print(driver.title)
print(driver.current_url)









time.sleep(10)