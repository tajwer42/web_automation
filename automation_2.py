from selenium import webdriver
import os
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def accept_js_popup():
    '''handle alert box'''
    alert_obj = driver.switch_to.alert
    alert_obj.accept()

def custom_wait_time(given_time):
    '''customized wait time'''
    time.sleep(given_time)

def go_to_home_page():
    '''go to home page module'''
    driver.find_element_by_xpath('//*[@id="navbarExample"]/ul/li[1]').click()

def login_module(test_user,test_password):
    '''login module'''
    
    driver.find_element_by_id('user-name').clear()
    driver.find_element_by_id('password').clear()
    custom_wait_time(4)
    username = driver.find_element_by_id("user-name")
    password = driver.find_element_by_id("password")

    username.send_keys(test_user)
    password.send_keys(test_password)
    driver.find_element_by_id('login-button').click()

url = 'https://www.saucedemo.com/'


PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
DRIVER_BIN = os.path.join(PROJECT_ROOT, "chromedriver")

driver = webdriver.Chrome(executable_path = DRIVER_BIN)

#test user and name
locked_user = "locked_out_user"
standard_user = "standard_user"
test_password = "secret_sauce"

#contact
test_email = "mtssimaa@gmail.com"
test_name = "siam"
test_message = "test message"

# open website with url
driver.get(url)

custom_wait_time(5)

#logi nwith locked user
login_module(locked_user,test_password)

texts = driver.find_element_by_xpath('//*[@id="login_button_container"]/div/form/h3').text

if (texts.strip()=="Epic sadface: Sorry, this user has been locked out."):
    print("This is the locked out user")
else:
    print("Case failed")

input('Press ENTER to close the automated browser')

driver.quit()

