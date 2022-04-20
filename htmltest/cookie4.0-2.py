import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import json,time,sys

driver = webdriver.Firefox()
url = 'http://wzk.36ve.com/login/login'
driver.get(url)
sleep(1)

user_loc = (By.ID,'loginform-username')
psw_loc = (By.ID,'loginform-password')
sumbit_loc = (By.CLASS_NAME,'login')

driver.find_element(*user_loc).send_keys('13651115151')

driver.find_element(*psw_loc).send_keys('12345678')
driver.find_element(*sumbit_loc).click()



'''
#cookie2 = driver.get_cookies()
#print(cookie2)
# 创建一个requests session对象
s = requests.Session()
# 从driver中获取cookie列表（是一个列表，列表的每个元素都是一个字典）
cookies = driver.get_cookies()
# 把cookies设置到session中
for cookie in cookies:
	s.cookies.set(cookie['name'],cookie['value'])
driver.close()

# 需要登录才能看到的页面URL
page_url = 'http://wzk.36ve.com/index.php/course/organize-course'
# 获取该页面的HTML
resp = s.get(page_url)
resp.encoding = 'utf-8'
'''

#driver.get(page_url)
#creat_course_loc = (By.ID,'createCourse')
sleep(3)
'''
try:
    driver.find_element(*creat_course_loc)
except Exception:
    print('未登陆')
else:
    print('找到元素--')
'''
cookie = driver.get_cookies()
print(cookie)
jsonCookies = json.dumps(cookie)
with open('qqhomepage.json', 'w') as f:
    f.write(jsonCookies)

driver.quit()

str=''
with open('qqhomepage.json','r',encoding='utf-8') as f:
    listCookies=json.loads(f.read())
cookie = [item["name"] + "=" + item["value"] for item in listCookies]
cookiestr = '; '.join(item for item in cookie)
print(cookiestr)


url = 'http://wzk.36ve.com/index.php/course/organize-course'
headers = {
    'cookie': cookiestr,
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0'
}
html = requests.get(url=url, headers=headers)
print(html.text)

#cookie3 = requests.
#print(cookie3)

