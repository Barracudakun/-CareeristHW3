
from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By


# @given('Launch chrome browser')
# def launchChromeBrowser(context):
#     context.driver = webdriver.Chrome('/Users/seashore/PycharmProjects/CareeristHW3/chromedriver')


# @when('Open Amazon page')
# def openAmazonPage(context):
#     context.driver.get('https://www.amazon.com')


@when('Input Table in search field')
def searchAmazon(context):
    context.driver.find_element(By.ID, 'twotabsearchtextbox').send_keys('Table')


@when(u'Click on Amazon search icon')
def clikcSearch(context):
    context.driver.find_element(By.ID, 'nav-search-submit-button').click()


@then(u'Verify search worked')
def verifySearch(context):
    # actual_result = context.driver.find_element(By.XPATH, "//span[@class='a-color-state a-text-bold']").text
    # expected_result = "Table"
    # assert expected_result in actual_result, f'Expected {expected_result}, but got {actual_result}'
    actual_result = context.driver.find_element(By.XPATH, "//span[@class='a-color-state a-text-bold']").is_displayed()
    assert actual_result is True

@then('Close Browser')
def closeBrowser(context):
    context.driver.quit()