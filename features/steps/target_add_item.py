from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@when('Click on item and add to cart')
def click_on_item_and_add_to_cart(context):
    context.driver.find_element(By. ID, "addToCartButtonOrTextIdFor89652980").click()
    sleep(5)

@then('Verify that the item is in the cart')
def verify_item_added_to_cart(context):
    actual_cart_text = context.driver.find_element(By.CSS_SELECTOR, "h4[class='sc-fe064f5c-0 ezqPcT']").text
    expected_cart_text = 'Your cart is empty'
    assert expected_cart_text not in actual_cart_text, f'Expected {expected_cart_text} to not be in {actual_cart_text}'
    print('Test case passed')


