from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


driver = webdriver.Firefox()
url = 'http://fyzyk.36ve.com'
driver.get(url)
cookie = driver.get_cookies()
print(cookie)
#driver.add_cookie({'name': '_csrf', 'value': '247e44e146e1f060477f34a94ba0b144186b1711edaf740a74369f08662d9dd7a%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22_csrf%22%3Bi%3A1%3Bs%3A32%3A%22AZZu_08HlkJNl6j9DISao3EawUdwc44Z%22%3B%7D', 'path': '/', 'domain': 'wzk.36ve.com', 'secure': False, 'httpOnly': True, 'sameSite': 'None'})
#driver.add_cookie({'name': 'LoginForm[username]', 'value': '13651115151'})
#driver.add_cookie({'name': 'LoginForm[password]', 'value': '25d55ad283aa400af464c76d713c07ad'})
#print(driver.get_cookie('PHPSESSID'))
#print(driver.get_cookie('_csrf'))
#driver.delete_all_cookies()
#cookie = driver.get_cookies()
#print(cookie)
#print('111')

#driver.add_cookie({'name': 'PHPSESSID','value': 'nr2h9jvfid35mp0du0mdbdbfer', 'path': '/', 'domain': 'wzk.36ve.com', 'secure': False, 'httpOnly': True, 'expiry': 1612432350, 'sameSite': 'None'})
#driver.add_cookie({'name': '_csrf', 'value': '247e44e146e1f060477f34a94ba0b144186b1711edaf740a74369f08662d9dd7a%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22_csrf%22%3Bi%3A1%3Bs%3A32%3A%22AZZu_08HlkJNl6j9DISao3EawUdwc44Z%22%3B%7D', 'path': '/', 'domain': 'wzk.36ve.com', 'secure': False, 'httpOnly': True, 'sameSite': 'None'})
'''
cookie = driver.get_cookies()
print(cookie)

html = driver.get('http://wzk.36ve.com/index.php/course/organize-course')
creat_course_loc = (By.ID,'createCourse')
try:
    driver.find_element(*creat_course_loc)
except Exception:
    print('未登陆')
else:
    print('找到元素--')
'''


sleep(3)
driver.quit()
