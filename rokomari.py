import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

# Initialize an empty dictionary
book_links = {}

for page in range(1, 4):  
    driver.get(f'https://www.rokomari.com/search?term=islamic+books&search_type=ALL&page={page}')
    driver.maximize_window()
    
    links = []
    
    for i in range(1, 5):
        book = str(i)
        try:
            link = driver.find_element(By.XPATH, '/html/body/div[8]/div/div/div/section[2]/div[2]/div/div[' + book + ']/div/a').get_attribute("href")
            links.append(link)
        except Exception as e:
            print(f"Error on page {page}, book {book}: {e}")
    
    book_links[f'page_{page}'] = links

print(book_links)

time.sleep(5)
driver.quit() 