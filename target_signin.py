from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# Setup ChromeDriver
driver_path = ChromeDriverManager().install()
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# Open the URL
driver.get("https://www.target.com/")

# Locate the Sign-In button using a valid XPath
sign_in_button = driver.find_element(By.XPATH, "//a[@data-test='@web/AccountLink']")
sign_in_button.click()

side_nav_signin_btn = driver.find_element(By.XPATH, "//button[@data-test='accountNav-signIn']")
side_nav_signin_btn.click()

sleep(5)

# Verify the text of the Sign-In button
expected_result = "Sign into your Target account"
actual_result = driver.find_element(By.XPATH, "//h1//span").text
assert expected_result == actual_result, f"Expected '{expected_result}', but got '{actual_result}'"
driver.find_element(By.ID, "login")
print("Test case passed!")


# Close the browser
driver.quit()





