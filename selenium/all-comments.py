from selenium import webdriver
import time
from selenium.webdriver.common.by import By 
import re

driver = webdriver.Chrome()

driver.maximize_window()

driver.get('https://www.alibaba.com/product-detail/14-inch-Win-10-11-brand_1600673527864.html?spm=a27aq.theme_tab_list.dt_1.1.627548daviku4d')

# Scroll to the bottom of the page
height = driver.execute_script("return document.body.scrollHeight")
print(height)
for i in range(0, height+1000, 100):
    driver.execute_script(f'window.scrollTo(0, {i})')
    time.sleep(0.5)

product_title = driver.find_element(By.XPATH, '//h1').text
print(f'Product Title: {product_title}')

# Get all reviews
all_reviews = driver.find_elements(By.CLASS_NAME, 'review-info')
for review in all_reviews:
    print(f'Reviews: {review.text}')
    

time.sleep(30)
driver.quit()