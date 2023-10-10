from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

# Create a Firefox WebDriver instance
driver = webdriver.Firefox()

# Open the website
website_url = 'https://svc.mt.gov/msl/mtcadastral/'
driver.get(website_url)

# Find and click the search button
search_button = driver.find_element(By.ID, 'searchButton')
search_button.click()

# Wait for the Subdivision option to load
subdivision_option = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//div[@id="subdivisionSearchPane_button"]'))
)

# Click the Subdivision option
subdivision_option.click()

# Wait for the County selection dropdown to be present
select_county = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, 'subdivisionCountySelect'))
)

# Use the Select class to interact with the dropdown
county_dropdown = Select(select_county)

# Wait for the option with visible text 'YELLOWSTONE' to be present
yellowstone_option = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, "//option[text()='YELLOWSTONE']"))
)

# Select the option by visible text
county_dropdown.select_by_visible_text('YELLOWSTONE')

# Wait for the options to load in the second dropdown
# You may need to adjust the waiting conditions based on the actual behavior of the page
second_dropdown_options = WebDriverWait(driver, 20).until(
    EC.presence_of_all_elements_located((By.XPATH, '//div[@id="subdivisionSearchPane"]//option'))
)

# Optionally, you can interact with the options in the second dropdown

# Close the browser window
driver.quit()
