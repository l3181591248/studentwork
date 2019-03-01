from selenium.webdriver.support.wait import WebDriverWait
from framwork.logger import Logger
from selenium.webdriver.support import expected_conditions as EC
import os
import time


logger=Logger(logger="Basic").getlog()
class Basic(object):
    def __init__(self,driver):
        self.driver=driver

    def log_in(self,url):
        self.driver.get(url)

    def back(self): #浏览器后退
        self.driver.back()
        logger.info("后退")

    def forward(self):# 浏览器前进
        self.driver.forward()
        logger.info("前进")

    def open_url(self,url):
        self.driver.get(url)
        #关闭浏览器
    def quit(self):
        self.driver.quit()
    #关闭窗口
    def close(self):
        try:
            self.driver.close()
            logger.info("关闭网页")
        except Exception as e:
            logger.error("关闭网页失败 %s"%e)
    #寻找元素
    def find_element(self,*loc):
        try:
            WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(loc))
            return self.driver.find_element(*loc)
            logger.info("找到页面元素——>", loc)
        except:
            logger.error("%s页面中未能找到%s元素——>"%(self,loc))
            return None
            #保存图片
    # def get_windows_img(self):
    #     file_path=os.path.dirname(os.path.abspath("."))+"/screenshots/"
    #     rq=time.strftime("%Y%m%d%H%N",time.localtime(time.time()))
    #     screen_name=file_path+rq+".png"
    #     try:
    #         self.driver.get_screenshot_as_file(screen_name)
    #     except Exception as e:
            # self.get_windows_img()
            # logger.error("Failed to the screenshot %s"%e)
    #清除文本框
    def clear(self,*loc):
        el=self.find_element(*loc)
        try:
            el.clear()
            logger.info("Clear text input box before typing ")
        except Exception as e:
            logger.error("Failed to type in input box with %s"%e)
    #输入
    def sendkeys(self,text,*loc):
        el=self.find_element(*loc)
        # el.clear()
        try:
            el.send_keys(text)
            logger.info("输入内容"+text)
        except Exception as e:
            logger.error("Failed to type in input box with %s"%e)
            # self.get_windows_img()
    #点击元素
    def click(self,*loc):
        el=self.find_element(*loc)
        try:
            el.click()
            logger.info("Clear text input box before typing")
        except Exception as e:
            logger.error("Failed to type in input box with %s" % e)

    def text(self,*loc):
        el = self.find_element(*loc)
        try:
            print(el.text)
            logger.info("已获取")
        except Exception as e:
            logger.error("未获取 %s" % e)
    #激活窗口
    def activation_window(self,n):
        self.driver.switch_to.window(self.driver.window_handles[n])
    #进入ifram