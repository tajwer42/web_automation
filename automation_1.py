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

url = 'https://www.demoblaze.com/index.html'


PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
DRIVER_BIN = os.path.join(PROJECT_ROOT, "chromedriver")

driver = webdriver.Chrome(executable_path = DRIVER_BIN)

#test user and name
test_user = "sa98765nbv6nncc"
test_pass = "1234"

#card information
test_card_name = "siam"
test_card_country = "BD"
test_card_city = "Dhaka"
test_card_no = "12324"
test_card_month = "12"
test_card_year = "2020"

#contact
test_email = "mtssimaa@gmail.com"
test_name = "siam"
test_message = "test message"

# open website with url
driver.get(url)

#wait for some time
element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "signin2"))
)

#click on sign up button
driver.find_element_by_id("signin2").click()

custom_wait_time(10)

#enter user name and password
username = driver.find_element_by_id("sign-username")
password = driver.find_element_by_id("sign-password")

username.send_keys(test_user)
password.send_keys(test_pass)

#click on submit button
driver.find_element_by_xpath('//*[@id="signInModal"]/div/div/div[3]/button[2]').click()

custom_wait_time(8)
accept_js_popup()

custom_wait_time(8)

#click on Log in button
driver.find_element_by_id("login2").click()

custom_wait_time(8)

#enter user name and password
username = driver.find_element_by_id("loginusername")
password = driver.find_element_by_id("loginpassword")

username.send_keys(test_user)
password.send_keys(test_pass)

#click on submit button
driver.find_element_by_xpath('//*[@id="logInModal"]/div/div/div[3]/button[2]').click()

custom_wait_time(10)

#click on phone category
driver.find_element_by_xpath('//*[@id="itemc"][1]').click()

custom_wait_time(5)
#click on a phone 
driver.find_element_by_xpath('//*[@id="tbodyid"]/div[1]/div/div/h4/a').click()

custom_wait_time(5)
#add to cart
driver.find_element_by_xpath('//*[@id="tbodyid"]/div[2]/div/a').click()

custom_wait_time(8)
accept_js_popup()
go_to_home_page()

custom_wait_time(5)
#click on Laptop category
driver.find_element_by_xpath('//*[@id="itemc"][2]').click()
custom_wait_time(5)
#click on a laptop 
driver.find_element_by_xpath('//*[@id="tbodyid"]/div[1]/div/div/h4/a').click()

#wait
custom_wait_time(5)
#add to cart
driver.find_element_by_xpath('//*[@id="tbodyid"]/div[2]/div/a').click()

custom_wait_time(5)
accept_js_popup()
go_to_home_page()

custom_wait_time(8)
#click on Monitor category
driver.find_element_by_xpath('//*[@id="itemc"][3]').click()
custom_wait_time(8)
#click on a monitor
driver.find_element_by_xpath('//*[@id="tbodyid"]/div[1]/div/div/h4/a').click()

#wait
custom_wait_time(8)
#add to cart
driver.find_element_by_xpath('//*[@id="tbodyid"]/div[2]/div/a').click()

custom_wait_time(8)
accept_js_popup()
go_to_home_page()

custom_wait_time(5)

#go to cart
driver.find_element_by_id("cartur").click()

custom_wait_time(5)

#get order value
order_value = driver.find_element_by_id("totalp").text

#print oder value
print(order_value)

#place order
driver.find_element_by_xpath('//*[@id="page-wrapper"]/div/div[2]/button').click()

#wait
custom_wait_time(5)

name = driver.find_element_by_id("name")
country = driver.find_element_by_id("country")
city = driver.find_element_by_id("city")
credt_card = driver.find_element_by_id("card")
month = driver.find_element_by_id("month")
year = driver.find_element_by_id("year")


name.send_keys(test_card_name)
country.send_keys(test_card_country)
city.send_keys(test_card_city)
credt_card.send_keys(test_card_no)
month.send_keys(test_card_month)
year.send_keys(test_card_year)


#click purchase
driver.find_element_by_xpath('//*[@id="orderModal"]/div/div/div[3]/button[2]').click()
custom_wait_time(5)

#copy amount
final_amount =driver.find_element_by_xpath('/html/body/div[10]/p').text
final_amount = final_amount.split(' ')
print(final_amount[2])



if (int(final_amount[2].strip()))== int(order_value):
    print("value matched")
else:
    print("Case failed")

#click ok
driver.find_element_by_xpath('/html/body/div[10]/div[7]/div/button').click()

custom_wait_time(5)

#click on contact
driver.find_element_by_xpath('//*[@id="navbarExample"]/ul/li[2]/a').click()

custom_wait_time(5)

#send values to contact
email_contact = driver.find_element_by_id("recipient-email")
recipient_contact = driver.find_element_by_id("recipient-name")
message_contact = driver.find_element_by_id("message-text")

email_contact.send_keys(test_email)
recipient_contact.send_keys(test_name)
message_contact.send_keys(test_message)

#send contact
driver.find_element_by_xpath('//*[@id="exampleModal"]/div/div/div[3]/button[2]').click()

custom_wait_time(8)
accept_js_popup()

custom_wait_time(5)

#logout
driver.find_element_by_id("logout2").click()

input('Press ENTER to close the automated browser')

driver.quit()

