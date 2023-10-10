from selenium import webdriver
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()
options.ignore_local_proxy_environment_variables()
# options.add_argument('--headless')
driver = webdriver.Chrome(options=options)
profile_url = 'https://www.depparts.com/'
driver.get(profile_url)

select_make = driver.find_element(By.CLASS_NAME, "brand")

select_make.click()
time.sleep(10)
# searching = driver.find_element(By.ID, "search")
# searching.send_keys('Rubber Tracks')