import streamlit as st
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

# Function to search Google and collect links
def search_google(query):
    # Setup Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run Chrome in headless mode

    # Initialize Selenium WebDriver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    # Open Google and search
    driver.get(f"https://www.google.com/search?q={query}")
    time.sleep(2)

    links = []

    # Loop through first three pages
    for page in range(1, 4):
        # Collect all link elements on the current page
        results = driver.find_elements(By.CSS_SELECTOR, 'a')

        # Extract the href attribute from each link
        for result in results:
            link = result.get_attribute('href')
            if link and "google" not in link:  # Avoid google internal links
                links.append(link)

        # Navigate to the next page if available
        try:
            next_button = driver.find_element(By.ID, "pnnext")
            next_button.click()
            time.sleep(2)
        except:
            break  # No more pages

    driver.quit()
    return links

# Streamlit app
st.title("Google Search Scraper")

# Input field for user query
query = st.text_input("Enter your search query:")

# Submit button
if st.button("Submit"):
    if query:
        with st.spinner('Searching Google...'):
            # Get search results
            result_links = search_google(query)
            st.success("Search Completed!")

            # Display results in table
            if result_links:
                st.write("Top results from Google:")
                st.table(result_links)
            else:
                st.warning("No results found.")
    else:
        st.warning("Please enter a search query.")
