from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

service = Service("YOUR PATH")
# THIS PREVENTS WINDOW FROM CLOSING
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
driver.get("https://en.wikipedia.org/wiki/Main_Page")
driver.maximize_window()

# Article_Count
article_count = driver.find_element(By.CSS_SELECTOR, value="#articlecount a")
# print(article_count.text)
# article_count.click()

# Find element by Link text
all_portals = driver.find_element(By.LINK_TEXT, value="Content portals")
# all_portals.click()

#Find the "Search" <input> by Name
search = driver.find_element(By.NAME, value="search")

# Sending keyboard input to Selenium
search.send_keys("Python", Keys.ENTER)

# driver.quit()
