from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)

# Find element, by ID:
driver.find_element(By. ID,  'ap_email')
driver.find_element(By. ID,  'continue')

# by XPATH, text():
driver.find_element(By. XPATH, "//*[text()='Conditions of Use']")
driver.find_element(By. XPATH, "//*[text()='Privacy Notice']")

# by XPATH, any tag, but with attributes=value
driver.find_element(By. XPATH, "//span[@class='a-expander-prompt']")

# Find element, by XPATH:
driver.find_element(By. XPATH,  "//a[@class='a-icon a-icon-logo']")
driver.find_element(By. XPATH, "//a[@id='auth-fpp-link-bottom']")
driver.find_element(By. XPATH, "//a[@id='ap-other-signin-issues-link']")
driver.find_element(By. XPATH, "//a[@id='createAccountSubmit']")