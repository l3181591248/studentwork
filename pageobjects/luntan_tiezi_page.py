from selenium.webdriver.common.by import By
from  framwork.Basics import Basic
import time
import unittest

class Homepage(Basic):
    home_page_input_username = (By.ID, "ls_username")  # 用户名
    home_page_input_pwd = (By.XPATH, "//input[@type='password']")  # 密码
    home_page_button_login = (By.CSS_SELECTOR, ".fastlg_l button")  # 登录
    home_page_button_quit = (By.LINK_TEXT, "退出")
    home_page_input_Search_box = (By.CSS_SELECTOR, ".scbar_txt_td input")  # 搜索框
    home_page_button_hunt_for=(By.XPATH,"//button[@type='submit']")   #搜索按钮
    home_page_button_hunt_search_result=(By.XPATH,'//li[@class="pbw"]//a ')#搜索结果
    home_page_get_subject = (By.CSS_SELECTOR, ".ts span")  # 搜索结果的标题

    def login(self,name,pwd):
        self.sendkeys(name, *self.home_page_input_username)  # 用户名
        self.sendkeys(pwd, *self.home_page_input_pwd)  # 密码
        self.click(*self.home_page_button_login)#登录

    def Logout(self):
        self.click(*self.home_page_button_quit)#退出登录
    def search(self,content):
        self.sendkeys(content,*self.home_page_input_Search_box)#搜索内容
        self.click(*self.home_page_button_hunt_for)  # 搜索
    def activation_window(self, n):
        self.driver.switch_to.window(self.driver.window_handles[n])#激活窗口
    def search_result(self):
        self.click(*self.home_page_button_hunt_search_result)#进入搜索结果
    def submit(self):
        self.driver.switch_to.window(self.driver.window_handles[2])
        self.click(*self.home_page_get_subject)
        m = self.driver.find_element_by_css_selector( ".ts span")
        return m.text
