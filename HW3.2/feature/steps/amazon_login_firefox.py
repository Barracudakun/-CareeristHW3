from selenium import webdriver
from behave import *
from selenium.webdriver.common.by import By
from time import sleep


@given('Launch Firefox browser')
def launchChromeBrowser(context):
    context.driver = webdriver.Firefox()

# @when('Open Amazon page')
# def openAmazonPage(context):
#     context.driver.get('https://www.amazon.com')
#
# @when('Click Amazon sign in section')
# def clickSignin(context):
#     context.driver.find_element(By.ID, "nav-link-accountList-nav-line-1").click()
#
# @when('Enter Email "{user}"')
# def enterEmail(context, user):
#     context.driver.find_element(By.ID, 'ap_email').send_keys(user)
#
#
# @when('Click Continue button')
# def clickButton(context):
#     context.driver.find_element(By.ID,'continue').click()
#
# @when('Enter Password "{pwd}"')
# def enterPassword(context,pwd):
#     context.driver.find_element(By.ID, 'ap_password').send_keys(pwd)
#
#
# @when('Click Sing-in button')
# def clickSignIn(context):
#     context.driver.find_element(By.ID, 'signInSubmit').click()
#     sleep(3)
#
# @then('User must successfully login the your account page')
# def verifyLoginPage(context):
#     expected_result = context.driver.find_element(By.XPATH, '//*[@id="glow-ingress-line1"]').text
#     assert "Yingxu" in expected_result