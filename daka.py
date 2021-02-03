#!/usr/bin/python
# -*- coding: UTF-8 -*-
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from apscheduler.schedulers.blocking import BlockingScheduler
import key
 
#打卡时间 小时、分钟
c_minute = "45" 
c_hour = "16"

#网址、用户名、密码
url = 'http://mapp.zjut.edu.cn/_web/_apps/eform/onlinesurvey/onlineSurvey_m.jsp?domainId=1&topicId=17'  #学生战役网址
username = key.username
password = key.password

def work():
	try:
		#打开浏览器
		browser = webdriver.Chrome()  #如使用的是Edge 请注释
		#browser = webdriver.Edge()
		browser.get(url)
		#输入python
		browser.find_element_by_id('username').clear()
		browser.find_element_by_id('username').send_keys(username)
		browser.find_element_by_id('password').clear()
		browser.find_element_by_id('password').send_keys(password) #password
		browser.find_element_by_class_name('sl-login-btn').click()
		browser.find_element_by_class_name('l-btn-text').click()
		time.sleep(2)
		browser.find_element_by_link_text('提交').click()
		browser.find_element_by_class_name('l-btn-text').click()
	
		#退出浏览器
		time.sleep(2)
		browser.quit()
		print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())+": Clock Success!")
	except:
		print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())+": Clock Filed!")

if __name__ == '__main__':
	#添加任务
	scheduler = BlockingScheduler()
	#设置定时任务时间
	scheduler.add_job(work,'cron', minute=c_minute,hour=c_hour)
	print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())+": Add Task Work!")
	try:
		scheduler.start()
	except (KeyboardInterrupt, SystemExit):
		scheduler.shutdown()

