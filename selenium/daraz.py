import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
# driver.get("https://www.daraz.com.bd/catalog/?spm=a2a0e.tm80335411.search.d_go&q=pc")
# driver.maximize_window()

link_list = []

for page in range(1, 3):
    driver.get(f'https://www.daraz.com.bd/catalog/?page={page}&q=pc&spm=a2a0e.tm80335411.search.d_go')
    driver.maximize_window()
    for product in range(1, 5):
        type_i = str(product)
        link = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div[1]/div/div[1]/div[2]/div['+type_i+']/div/div/div[2]/div[2]/a').get_attribute("href")
        link_list.append(link)

print(link_list)
driver.get(link.get_attribute("href"))

time.sleep(10)