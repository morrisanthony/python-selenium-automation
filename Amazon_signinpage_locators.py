from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)

# CSS, by class:
driver.find_element(By.CSS_SELECTOR, "a[class='a-link-nav-icon']")
driver.find_element(By.CSS_SELECTOR, "h1[class='a-spacing-small']")
driver.find_element(By. CSS_SELECTOR, "div[class='a-box-inner a-alert-container']")
driver.find_element(By.CSS_SELECTOR, "input[class='a-button-input']")
driver.find_element(By.CSS_SELECTOR, "a[class='a-link-emphasis']")


#CSS, by ID:
driver.find_element(By.CSS_SELECTOR, "input[id='ap_customer_name']")
driver.find_element(By.CSS_SELECTOR, "input[id='ap_email']")
driver.find_element(By.CSS_SELECTOR, "input[id='ap_password']")
driver.find_element(By.CSS_SELECTOR, "input[id='ap_password_check']")


# by CSS, attr partial match
driver.find_element(By.CSS_SELECTOR, "a[href*='ap_register_notification_condition_of_use']")
driver.find_element(By.CSS_SELECTOR, "a[href*='ap_register_notification_privacy_notice']")

