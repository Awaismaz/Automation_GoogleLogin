import undetected_chromedriver as webdriver
# from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

# Replace with your actual URL
driver.get("https://www.google.com")

signin_link = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "gb_ma"))
)

href = signin_link.get_attribute('href')


driver.get(href)

email_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "identifierId"))
)
email_input.clear()
email_input.send_keys("address@gmail.com")
email_input.send_keys(Keys.ENTER)

pass_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "Passwd"))
)
pass_input.clear()
pass_input.send_keys("Password")
pass_input.send_keys(Keys.ENTER)

while True:
    pass