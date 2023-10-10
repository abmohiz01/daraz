import openpyxl
import pandas as pd

from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.ignore_local_proxy_environment_variables()
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)

website = "https://www.daraz.pk/smartphones/"
driver.get(website)

results = driver.find_element(By.CLASS_NAME, 'box--ujueT')
result_list = results.find_elements(By.XPATH, '*')

product_list = []
for product in result_list:
    product_data = {
        'title': product.find_element(By.CLASS_NAME, 'title--wFj93').get_attribute('innerText'),
        'price': product.find_element(By.CLASS_NAME, 'currency--GVKjl').get_attribute('outerText')
    }
    product_list.append(product_data)

driver.quit()

# Convert the list of dictionaries into a pandas DataFrame
df = pd.DataFrame(product_list)

# Save the DataFrame to an Excel file
excel_file = 'scraped_data.xlsx'
df.to_excel(excel_file, index=False)

print("Data saved to", excel_file)
