import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import json,time,sys

driver = webdriver.Firefox()
url = 'http://fyzyk.36ve.com/?q=custom_user_login'
driver.get(url)
sleep(1)

#user_loc = (By.ID,'username')
#psw_loc = (By.ID,'psd')
#sumbit_loc = (By.CLASS_NAME,'login_btn')

#driver.find_element(*user_loc).send_keys('13611111111')
#driver.find_element(*psw_loc).send_keys('12345678')
#driver.find_element(*sumbit_loc).click()

#driver.add_cookie({'name': 'SESS74033f41303334d9a6e0f813d37f56ef', 'value': 'FI2_8N6-ThpAsi7o2Zaf6ULeSjf8E2QHiWWKAT8UXdg', 'path': '/', 'domain': '.fyzyk.36ve.com', 'secure': False, 'httpOnly': True, 'expiry': 1614410470, 'sameSite': 'None'})

sleep(2)

#需要登录的url
#driver.delete_all_cookies()
driver.add_cookie({'name': 'user_sys_key', 'value': 'JINaINGnHLHZCxmfJLx3Ts1245ebVBzUZv7mrB_1XDgIkCpByzM-i3kBfe1gJs1S2mD84iyIAhKx8gL4BaIQHbRr0KDPp0DLWwDYtt4Y_uQgjqYfTtDPCiO7ElSpht5I-dCEwREf9wIMq22', 'path': '/', 'domain': 'fyzyk.36ve.com', 'secure': False, 'httpOnly': False, 'expiry': 1612506252, 'sameSite': 'None'})
#driver.add_cookie({'name': 'login_flag', 'value': '0', 'path': '/', 'domain': 'fyzyk.36ve.com', 'secure': False, 'httpOnly': True, 'sameSite': 'None'},)
driver.add_cookie({'name': 'uc_local_login', 'value': '2', 'path': '/', 'domain': 'fyzyk.36ve.com', 'secure': False, 'httpOnly': True, 'sameSite': 'None'})
driver.add_cookie({'name': 'uc_uid', 'value': '10643', 'path': '/', 'domain': 'fyzyk.36ve.com', 'secure': False, 'httpOnly': False, 'expiry': 1612506252, 'sameSite': 'None'})
driver.add_cookie({'name': 'SESS74033f41303334d9a6e0f813d37f56ef', 'value': 'fLGIEb20JL7MX1ZkqMG8kn24MHzHkm4u6VWIHff_tPg', 'path': '/', 'domain': '.fyzyk.36ve.com', 'secure': False, 'httpOnly': True, 'expiry': 1612506252, 'sameSite': 'None'})
driver.add_cookie({'name': 'major_id', 'value': '30', 'path': '/', 'domain': 'fyzyk.36ve.com', 'secure': False, 'httpOnly': False, 'sameSite': 'None'})

cookie = driver.get_cookies()
print(cookie)

page_url = 'http://fyzyk.36ve.com/?q=user/10643/editing'
driver.get(page_url)
driver.get(page_url)
sleep(2)

logout_loc = (By.XPATH,'//input[@value="退出登录"]')
create_course_loc = (By.CLASS_NAME,'create-course')
try:
    driver.find_element(*create_course_loc).click()
except Exception:
    print('未登陆')
else:
    print('找到元素--')

#driver.delete_all_cookies()
sleep(2)
driver.quit()


