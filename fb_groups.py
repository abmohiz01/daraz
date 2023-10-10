from selenium import webdriver
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()
options.ignore_local_proxy_environment_variables()
# options.add_argument('--headless')
driver = webdriver.Chrome(options=options)
profile_url = 'https://www.facebook.com'
driver.get(profile_url)
time.sleep(2)
email_field = driver.find_element(By.ID, "email")
email_field.send_keys('mohiz.a@yahoo.com')
time.sleep(1)
passwd_field = driver.find_element(By.ID, "pass")
passwd_field.send_keys('Abmohiz2001')
time.sleep(3)
login_button = driver.find_element(By.NAME, "login")
login_button.submit()
time.sleep(10)
passwd_field = driver.find_element(By.ID, "pass")
passwd_field.send_keys('Abmohiz2001')
login_button = driver.find_element(By.NAME, "login")
login_button.submit()

# Add a delay to allow time for the redirection to the profile
time.sleep(10)

# Now you can proceed to visit the profile
driver.get("https://www.facebook.com/abdul.mohiz.9465/")

# Rest of your code...
