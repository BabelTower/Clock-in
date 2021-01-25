# 每日一报（浙江工业大学）

## 配置环境

1. 安装selenium+apscheduler

```shell
pip3 install selenium
pip3 install apscheduler
```

2. [ChromeDriver-Mac安装](https://www.cnblogs.com/lilyo/p/11959494.html)

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

