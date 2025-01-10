from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

@given('Open target circle page')
def open_circle_page(context):
    context.driver.get('https://target.com/circle')

@when('Inspect page for the element that shows 10 benefit cells')
def inspect_page(context):
    benefit_cells = (By.XPATH, "//div[@class='cell-item-content']")
    context.driver.wait.until(EC.visibility_of_element_located(benefit_cells))


@then('Verify at least 10 benefit cells')
def verify_cells(context):
    expected_cells = 10
    actual_cells = len(context.driver.find_elements(By.XPATH, "//div[@class='cell-item-content']"))
    assert actual_cells >= expected_cells, f'Expected at least {expected_cells} cells, but found {actual_cells}'
    print('Test case passed')


