import time
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
browser.maximize_window()
wait = WebDriverWait(browser, 30)

USERNAME = '936844218@qq.com'
PASSWORD = '110huazhicai'


def login(url):
    try:
        browser.get(url)
        # 输入
        username = browser.find_element_by_name('username')
        time.sleep(2)
        username.send_keys(USERNAME)
        password = browser.find_element_by_name('password')
        time.sleep(2)
        password.send_keys(PASSWORD)
        submit = browser.find_element_by_xpath('//*[@id="root"]/div/main/div/div/div/div[2]/div[1]/form/button')
        time.sleep(1)
        submit.click()
    except:
        print('login failed!')


if __name__ == '__main__':
    login('https://www.zhihu.com/signin?next=%2F')
