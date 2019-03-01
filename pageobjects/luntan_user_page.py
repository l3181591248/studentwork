from selenium.webdriver.common.by import By
from  framwork.Basics import Basic
import time

class Homepage(Basic):
    home_page_input_username = (By.ID, "ls_username")  # 用户名
    home_page_input_pwd = (By.XPATH, "//input[@type='password']")  # 密码
    home_page_button_Default_block = (By.CSS_SELECTOR, ".fl_tb a")  # 默认版块
    home_page_button_vote = (By.ID, "newspecial")  # 发帖
    home_page_input_title = (By.ID, "subject")  # 标题
    home_page_input_content = (By.ID, "fastpostmessage")  # 内容
    home_page_button_login = (By.CSS_SELECTOR, ".fastlg_l button")  # 登录
    home_page_button_quit = (By.LINK_TEXT, "退出")
    home_page_button_Submission = (By.CSS_SELECTOR, ".pnpost button")  # 提交



    def login(self,name,pwd):
        self.sendkeys(name, *self.home_page_input_username)  # 用户名
        self.sendkeys(pwd, *self.home_page_input_pwd)  # 密码
        self.click(*self.home_page_button_login)#登录
    def Logout(self):
        self.click(*self.home_page_button_quit)#退出登录
    def content(self,content):
        self.sendkeys(content,*self.home_page_input_content)#发帖/回复内容
    def Default_block(self):
        self.click(*self.home_page_button_Default_block)#点击默认版块
    def title(self,content):
        self.sendkeys(content,*self.home_page_input_title)#发帖题目
    def Submission(self):
        self.click(*self.home_page_button_Submission)
