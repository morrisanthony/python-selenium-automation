from behave import given, when, then
from selenium.webdriver.common.by import By
from time import sleep


@given('Open target page')
def open_main(context):
    context.driver.get('https://target.com/')


@when('click on cart icon')
def click_cart(context):
    context.driver.find_element(By.CSS_SELECTOR, "a[data-test='@web/CartLink']").click()
    sleep(5)


@then('Verify Your cart is empty')
def verify_cart_is_empty(context):
    expected_cart_text = 'Your cart is empty'
    sleep(5)
    actual_cart_text = context.driver.find_element(By.CSS_SELECTOR, "h1[class='sc-fe064f5c-0 fJliSz']").text
    assert expected_cart_text in actual_cart_text, f'Expected {expected_cart_text} to be in {actual_cart_text}'
    print('Test case passed')
