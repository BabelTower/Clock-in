#!/usr/bin/python
# -*- coding: UTF-8 -*-
import time
import requests
from selenium import webdriver
#from dingtalkchatbot.chatbot import DingtalkChatbot #如需使用钉钉推送，请取消注释
from selenium.webdriver.chrome.options import Options

#网址、用户名、密码
url = 'http://mapp.zjut.edu.cn/_web/_apps/eform/onlinesurvey/onlineSurvey_m.jsp?domainId=1&topicId=17'  #学生战役网址
username = '账号'
password = '密码'
# WebHook地址(如需钉钉推送成功，请取消注释)
#webhook = 'https://oapi.dingtalk.com/robot/send?access_token=填写WebhookTOKEN'
#secret = 'SEC0f4f476c**************'  # 可选：创建机器人勾选“加签”选项时使用
# 初始化机器人(如需钉钉推送成功，请取消注释)
#FlyBot = DingtalkChatbot(webhook, secret=secret)  # 方式二：勾选“加签”选项时使用（v1.5以上新功能）

try:
    requests.get(webhook, verify=False) #解决https出现的SSL问题
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
except:
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())+": Clock Default!")
    #FlyBot.send_text(msg = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())+": 很抱歉，今天的每日一报失败了!", is_at_all=False) #如需钉钉推送成功，请取消注释
else:
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())+": Clock Success!")
    #FlyBot.send_text(msg = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())+": 今天已经帮你完成每日一报啦！", is_at_all=False) #如需钉钉推送成功，请取消注释
