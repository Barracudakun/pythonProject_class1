'''
2. Practice with locators.
Create locators + search strategy for these page elements of Amazon Sign in page:
Amazon logo
Email field
Continue button
Need help link
Forgot your password link
Other issues with Sign-In link
Create your Amazon account button
*Conditions of use link
*Privacy Notice link


For example:
Email field, search by ID, “ap_email”
'''

# Create locators + search strategy for these page elements of Amazon Sign in page:
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

#chromedriver installed into my download file
driver = webdriver.Chrome('/Users/seashore/Dropbox/My Mac (MacBook-Air.lan)/Downloads/chromedriver')
#open amazon page
url = driver.get('http://www.amazon.com')
#maximize window
driver.maximize_window()
#implicitly_wait 10 second
driver.implicitly_wait(10)
# search strategy for these page elements of Amazon Sign in page
driver.find_element(By.ID, 'nav-link-accountList-nav-line-1').click()

# Amazon logo
driver.find_element(By.CSS_SELECTOR, '.a-icon-logo').click()
driver.back()

# Email field
driver.find_element(By.ID, 'ap_email').send_keys('yingxukun@gmail.com')
driver.find_element(By.ID, 'continue').click()
sleep(3)
driver.back()

# Need help link
driver.find_element(By.XPATH, "//span[@class='a-expander-prompt']").click()
sleep(2)
# driver.find_element(By.LINK_TEXT, 'Need help?').click()
# driver.find_element(By.PARTIAL_LINK_TEXT, 'Need help').click()

#Forgot your password link
driver.find_element(By.ID, 'auth-fpp-link-bottom').click()
sleep(2)
driver.back()

#first step to click the Need help link
driver.find_element(By.XPATH, "//span[@class='a-expander-prompt']").click()
#then Other issues with Sign-In link
driver.find_element(By.ID, 'ap-other-signin-issues-link').click()
sleep(2)
driver.back()

# Create your Amazon account button
driver.find_element(By.CSS_SELECTOR, '#createAccountSubmit').click()
sleep(2)
driver.back()

#*Conditions of use link
driver.find_element(By.XPATH, '//a[text()="Conditions of Use"]').click()
driver.back()
sleep(2)
#*Privacy Notice link
driver.find_element(By.XPATH, "//a[contains(@href,'ap_signin_notification_privacy_notice')]").click()
sleep(2)

driver.quit()
