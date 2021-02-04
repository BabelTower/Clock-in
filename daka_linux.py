#!/usr/bin/python
# -*- coding: UTF-8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

#网址、用户名、密码
url = 'http://mapp.zjut.edu.cn/_web/_apps/eform/onlinesurvey/onlineSurvey_m.jsp?domainId=1&topicId=17'  #学生战役网址
username = '学号'
password = '密码'

chrome_options = Options()
chrome_options.add_argument('--headless')  # 无界面
chrome_options.add_argument('--no-sandbox')  # 解决DevToolsActivePort文件不存在报错问题
chrome_options.add_argument('--disable-gpu')   # 禁用GPU硬件加速。如果软件渲染器没有就位，则GPU进程将不会启动。chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--window-size=1920,1080')  # 设置当前窗口的宽度和高度

browser = webdriver.Chrome('chromedriver',chrome_options=chrome_options)
browser.implicitly_wait(10) #使用implicitly_wait来指定最大等待时间，取消使用sleep这不灵活的方式
browser.get(url)
#输入python
browser.find_element_by_id('username').clear()
browser.find_element_by_id('username').send_keys(username)
browser.find_element_by_id('password').clear()
browser.find_element_by_id('password').send_keys(password) #password
browser.find_element_by_class_name('sl-login-btn').click()
browser.find_element_by_class_name('l-btn-text').click()
browser.find_element_by_link_text('提交').click()
browser.find_element_by_class_name('l-btn-text').click()
#退出浏览器
browser.quit()
print('success!')
