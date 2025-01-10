from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep

@given('Open target main page')
def open_main(context):
    context.driver.get('https://target.com/')

@when('search for tea')
def search_product(context):
    context.driver.find_element(By.ID, "search").send_keys('tea')
    context.driver.find_element(By.CSS_SELECTOR, "//a[data-test='@web/Search/SearchButton']").click()
    context.driver.wait.until(EC. visibility_of_element_located((By.ID, "searchResults")))

@then ('Verify search results shown')
def verify_search_results(context):
    expected_tea = 'tea'
    sleep(5)
    actual_results = context.driver.find_element(By.ID, "searchResults")
    assert expected_tea in actual_results, f'Expected {expected_tea} to be in {actual_results}'
    print('Test case passed')
