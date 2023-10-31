from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome() 
driver.get("http://www.google.com")
element = driver.find_element(By.CLASS_NAME,"gLFyf")
element.send_keys("TKUIM")
element.send_keys(Keys.RETURN)

driver.implicitly_wait(10)

search = driver.find_elements(By.XPATH,'//h3')
for result in search:
    print(result.text)
driver.quit