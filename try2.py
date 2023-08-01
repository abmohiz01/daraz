import pprint

from selenium import webdriver
from collections import OrderedDict
# path = 'D:\ScrappingWithSelenium\drivers\chromedriver.exe'
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.ignore_local_proxy_environment_variables()
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)
website = "https://www.daraz.pk/smartphones/?page=2"
driver.get(website)
print(driver.current_url)
# driver.find_element(By.ID)


# get the main search result ELEMENT
results = driver.find_elements(By.CLASS_NAME, 'inner--SODwy cursor-hover')

# get all product containers
result_list = results.find_elements(By.XPATH, '*')

# for each product, extract the title and price
titles = [product.find_element(By.CLASS_NAME, 'title--wFj93') for product in result_list]
prices = [product.find_element(By.CLASS_NAME, 'currency--GVKjl') for product in result_list]

product_list = []
for product in result_list:
    od = OrderedDict()
    od['title'] = product.find_element(By.CLASS_NAME, 'title--wFj93').get_attribute('innerText')
    od['price'] = product.find_element(By.CLASS_NAME, 'currency--GVKjl').get_attribute('outerText')
    product_list.append(od)

pprint.pprint(product_list)
