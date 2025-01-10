from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


@when('Click on item and add to cart')
def click_on_item_and_add_to_cart(context):
    ADD_CART_BUTTON = (By.CSS_SELECTOR, '[id*="addToCartButtonOrTextId"]')

    #context.driver.find_element(By. CSS_SELECTOR, "addToCartButtonOrTextIdFor").click()
    context.driver.wait.until(EC.element_to_be_clickable(ADD_CART_BUTTON)).click()
    #sleep(5)
   # context.driver.find_element(By.XPATH, "//button[@data-test='orderPickupButton']").click()
    #sleep(5)
    #context.driver.find_element(By. CSS_SELECTOR, 'a[href="/cart"]').click()
    #sleep(5)


@when('Confirm add to cart button on side navigation bar')
def confirm_add_to_cart_button(context):
    #sleep(5)
    SIDENAV_ADD_CART_BTN = (By.CSS_SELECTOR, '[data-test="orderPickupButton"]')
    context.driver.wait.until(EC.visibility_of_element_located(SIDENAV_ADD_CART_BTN)).click()
    #context.driver.find_element(By. CSS_SELECTOR, "addToCartButtonOrTextIdFor").click()
    #sleep(5)

@given('Search for coffee')
def search_for_coffee(context):
    context.driver.find_element(By.ID, "search").send_keys('coffee')
    context.driver.find_element(By.CSS_SELECTOR, '[data-test="@web/Search/SearchButton"]').click()
    sleep(10)

@when('Open the cart page')
def open_cart_page(context):
    context.driver.get('https://target.com/cart')
    context.driver.implicitly_wait(10)
   # sleep(5)

@then('Verify that the item is in the cart')
def verify_item_added_to_cart(context):
    actual_cart_text = context.driver.find_element(By.CSS_SELECTOR, '[class="h-margin-b-tight h-text-grayDark "]').text
    expected_cart_text = '1 item'
    assert expected_cart_text in actual_cart_text, f'Expected {expected_cart_text} to not be in {actual_cart_text}'
    print('Test case passed')


