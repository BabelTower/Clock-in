# 每日一报（浙江工业大学）

## 配置环境

1. 安装selenium+apscheduler

```shell
pip3 install selenium
pip3 install apscheduler
```

2. [ChromeDriver-Mac安装](https://www.cnblogs.com/lilyo/p/11959494.html)<br>[WebDriver-Edge](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/) (使用Edge请按照浏览器版本下载并放置在脚本同目录)

### linux配置（以centos7为例）

1.安装selenium、谷歌浏览器
```shell
pip install selenium
yum install google-chrome-stable_current_x86_64.rpm
```
安装完成之后，检查谷歌版本号
```shell
google-chrome -version
```

2.根据谷歌浏览器版本安装驱动器
```shell
wegt https://chromedriver.storage.googleapis.com/88.0.4324.96/chromedriver_linux64.zip  #请将88.0.4324.96修改为你的浏览器版本
unzip chromedriver_linux64.zip #解压zip
mv chromedriver /usr/bin/
chromedriver --version #查看chromedriver版本号
```

3.linux使用crontab来执行定时任务
```shell
30 8 * * * python daka_linux.py
```

## 参数设置

1. 删除代码行`import key`
2. 设置每日打卡时间

```c++
#打卡时间 小时、分钟
c_minute = "00" 
c_hour = "8"
```

3. 输入网址、学号、密码

```c++
#网址、学号、密码
url = 学生战役页面的网址
username = 学号
password = 密码
```

## 运行

后台运行

```shell
nohup python3 daka.py &
```

查看运行的后台进程

```shell
jobs -l
```

终止后台运行的进程

```shell
kill -9 进程号
```

参考教程：

1. [python之网页自动打卡](https://blog.csdn.net/lee1169639/article/details/77336463?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-1.control&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-1.control)
2. [nohup和&后台运行，进程查看及终止](https://www.cnblogs.com/baby123/p/6477429.html)
3. [ChromeDriver-Mac安装](https://www.cnblogs.com/lilyo/p/11959494.html)

