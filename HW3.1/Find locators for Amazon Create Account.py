from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome('/Users/seashore/Dropbox/My Mac (MacBook-Air.lan)/Downloads/chromedriver')
url = driver.get('https://www.amazon.com/ap/register?showRememberMe=true&openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Ftag%3Damazusnavi-20%26hvadid%3D381823327672%26hvpos%3D%26hvnetw%3Dg%26hvrand%3D15719455245557901507%26hvpone%3D%26hvptwo%3D%26hvqmt%3De%26hvdev%3Dc%26hvdvcmdl%3D%26hvlocint%3D%26hvlocphy%3D9028321%26hvtargid%3Dkwd-10573980%26ref%3Dnav_ya_signin%26hydadcr%3D28883_11845445%26gclid%3DEAIaIQobChMI0drXocXh8QIV1W5vBB2uBwvLEAAYASAAEgLfdfD_BwE&prevRID=2F4N38K98V6MB0JJMKR4&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&prepopulatedLoginId=&failedSignInCount=0&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&pageId=usflex&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0')
driver.maximize_window()
driver.implicitly_wait(10)


# amazon logo
driver.find_element(By.CSS_SELECTOR, '.a-icon-logo').click()  # .a-icon-logo[aria-label="Amazon"]  also work
driver.back()
sleep(2)

# create account
text = driver.find_element(By.CSS_SELECTOR, '#ap_register_form h1').text
print(text)
sleep(2)

# your name
driver.find_element(By.ID, 'ap_customer_name').send_keys('0987654321')
sleep(2)

# e-mail
driver.find_element(By.CSS_SELECTOR, '#ap_email').send_keys('1234567890')
sleep(2)

# password
driver.find_element(By.XPATH, '//input[@id = "ap_password"]').send_keys('000000')

# reenter-password
driver.find_element(By.ID, 'ap_password_check').send_keys('000000')

# button Create your amazon Account
driver.find_element(By.ID, 'continue').click()
sleep(3)

# term and conditions
# "//a[contains(@href, 'ap_register_notification_condition_of_use')] for stable xpath
driver.find_element(By.XPATH, '//div[@id="legalTextRow"]/a[1]').click()
driver.back()
sleep(3)

driver.quit()


