from behave import given, when, then
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support import expected_conditions as EC


@when('Click sign in')
def click_sign_in(context):
    #context.driver.find_element(By.ID, "account-sign-in").click()
    sign_in_btn = (By.ID, "account-sign-in")
    context.driver.wait.until(EC.element_to_be_clickable(sign_in_btn)).click()
    #sleep(5)

@given('From right side navigation menu, click Sign In')
def click_sign_in_from_menu(context):
    context.driver.find_element(By.XPATH, "//button[@data-test='accountNav-signIn']").click()
    sleep(5)

@then('Verify Sign in form opened')
def verify_sign_in_form(context):
    expected_sign_in_text = 'Sign into your Target account'
    sleep(5)
    actual_sign_in_text = context.driver.find_element(By.XPATH, "//span[text()='Sign into your Target account']").text
    assert expected_sign_in_text in actual_sign_in_text, f'Expected {expected_sign_in_text} to be in {actual_sign_in_text}'
    print('Test case passed')

