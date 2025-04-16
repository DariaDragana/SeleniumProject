from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

service = Service("YOUR PATH")
# THIS PREVENTS WINDOW FROM CLOSING
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
driver.get("https://secure-retreat-92358.herokuapp.com/")
driver.maximize_window()

first_name = driver.find_element(By.NAME, value="fName")
first_name.send_keys("wahwah")

second_name = driver.find_element(By.NAME, value="lName")
second_name.send_keys("wahahaha")

email = driver.find_element(By.NAME, value="email")
email.send_keys("wewe@gmail.com")

button = driver.find_element(By.TAG_NAME, value="button")
button.click()

