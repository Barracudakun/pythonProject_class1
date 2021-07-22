from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
driver = webdriver.Chrome('/Users/seashore/PycharmProjects/pythonProject/chromedriver')
driver.get('http://www.amazon.com')
driver.find_element_by_id('twotabsearchtextbox').send_keys('shoes')
sleep(2)
driver.find_element(By.ID, 'nav-search-submit-button').click()
sleep(2)
driver.quit()