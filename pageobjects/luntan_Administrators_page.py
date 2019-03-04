import time

from selenium.webdriver.common.by import By

from framwork.Basics import Basic


class Homepage(Basic):
    home_page_input_username = (By.ID, "ls_username")  # 用户名
    home_page_input_pwd = (By.XPATH, "//input[@type='password']")  # 密码
    home_page_button_Default_block = (By.CSS_SELECTOR, ".fl_tb a")  # 默认版块
    home_page_button_vote = (By.ID, "newspecial")  # 发帖
    home_page_input_title = (By.ID, "subject")  # 标题
    home_page_input_content = (By.ID, "fastpostmessage")  # 内容
    home_page_button_login = (By.CSS_SELECTOR, ".fastlg_l button")  # 登录
    home_page_button_quit = (By.LINK_TEXT, "退出")
    home_page_button_delet_choice = (By.XPATH, "//input[@type='checkbox']")  # 选择删除的内容
    home_page_button_delet = (By.PARTIAL_LINK_TEXT, "删除")
    home_page_button_delet_yes = (By.CSS_SELECTOR, ".tm_c button")  # 删除确定
    home_page_button_administration_center = (By.PARTIAL_LINK_TEXT, "管理中心")
    home_page_button_refer=(By.XPATH,"//input[@value='提交']")#管理中心--->登录时的提交
    home_page_button_luntan=(By.LINK_TEXT,"论坛")
    home_page_button_xinbankuai=(By.CSS_SELECTOR,".lastboard a") #添加新版块
    home_page_input_xinbankuai = (By)
    home_page_button_Submission = (By.CSS_SELECTOR, ".pnpost button")  # 提交
    home_page_button_xinbankuaifatie=(By.XPATH,"//div[@class='bm_c']/table/tbody/tr[2]/td[2]/h2/a")  #新版块发帖
    home_page_button_forum = (By.ID, "header_forum")    #论坛
    home_page_get_subject = (By.CSS_SELECTOR, ".ts span")  # 搜索结果的标题

    def pwd(self, content):
        self.sendkeys(content, *self.home_page_input_pwd)
    def login(self,name,pwd):
        self.sendkeys(name, *self.home_page_input_username)  # 用户名
        self.sendkeys(pwd, *self.home_page_input_pwd)  # 密码
        self.click(*self.home_page_button_login)#登录
    def Logout(self):
        self.click(*self.home_page_button_quit)  # 退出登录
    def delet_choice(self): #删除帖子
        self.click(*self.home_page_button_delet_choice)
        time.sleep(1)
        self.click(*self.home_page_button_delet)
        time.sleep(1)
        self.click(*self.home_page_button_delet_yes)
    def administration_center(self):
        self.click(*self.home_page_button_administration_center)#进入管理中心
    def refer(self):
        self.click(*self.home_page_button_refer)#管理中心页面的提交按钮
    def forum(self):
        self.click(*self.home_page_button_forum)#点击论坛
    def activation_window(self, n):
        self.driver.switch_to.window(self.driver.window_handles[n])#激活窗口
    def luntan(self):
        self.click(*self.home_page_button_luntan)
    def xinbankuai(self):
        self.click(*self.home_page_button_xinbankuai)#点击新版块
    def ifram(self,m):
        self.driver.switch_to.frame(m)
    def goin_xinbankuai(self):
        self.click(*self.home_page_button_xinbankuaifatie)#进入新版块
    def Default_block(self):
        self.click(*self.home_page_button_Default_block)#点击默认版块

    def fatie_title(self, content):
        self.sendkeys(content,*self.home_page_input_title)#发帖题目
    def Submission(self):
        self.click(*self.home_page_button_Submission)
    def content(self,content):
        self.sendkeys(content,*self.home_page_input_content)#发帖/回复内容

    def submit(self):
        self.driver.switch_to.window(self.driver.window_handles[2])
        self.click(*self.home_page_get_subject)
        m = self.driver.find_element_by_css_selector(".ts span")
        return m.text

    def find_id(self):
        a = self.driver.find_element_by_css_selector(".vwmy a")
        return a.text

    def find_bankuai(self):
        a = self.driver.find_element_by_xpath("//div[@id='pt']/div/a[4]").text
        return a

    def find_zhongxin(self):
        # a=self.driver.find_element_by_css_selector(".nav ul li em a").text
        a = self.driver.title
        return a

    def find_huitie(self):
        a = self.driver.find_element_by_xpath(
            "//div[@id='postlistreply']/div/table/tbody/tr/td[2]/div[2]/div/div/table/tbody").text
        return a

    def find_title(self):
        a = self.driver.find_element_by_css_selector(".ts").text
        return a

    def find_zhongxin_id(self):
        a = self.driver.find_element_by_xpath("//form[@id='loginform']/p[2]").text
        return a
