import os
from appium import webdriver

apk_path=os.path.dirname(os.path.abspath("."))

desired_caps={}
desired_caps['platformName']="Android"  #设备系统
desired_caps['platformVersion']='5.1.1'    #设备系统版本
desired_caps['deviceName']='127.0.0.1:62001'           #设备名称
desired_caps['sessionOverride']=True

desired_caps['app']=apk_path+'/app/todolist.apk'    #测试的apk路径
desired_caps['noReset']=True        #不需要每次都安装apk
#如果设置的是APP包的路径，则不需要配apppackage和appactivity   同理相反
desired_caps['appPackage']='com.example.todolist'
desired_caps['appActicity']='com.example.todolist.LoginActivity'

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)    #启动APP
driver.find_element_by_id('com.example.todolist:id/nameET').send_keys('1')
driver.find_element_by_id('com.example.todolist:id/passwordET').send_keys('1')
driver.find_element_by_id('com.example.todolist:id/loginBtn').click()
