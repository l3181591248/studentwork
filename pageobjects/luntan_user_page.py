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
    home_page_button_Submission = (By.CSS_SELECTOR, ".pnpost button")  # 提交
    home_page_get_subject = (By.CSS_SELECTOR, ".ts span")  # 搜索结果的标题

    # home_page_text_yonghu=(By.XPATH,"//div[@id='hd']/div/div/div/p/strong/a")   #获取用户名称
    home_page_text_yonghu = (By.CSS_SELECTOR, ".vwmy a")
    home_page_text_bankuai = (By.XPATH, "//div[@id='pt']/div/a[4]")  # 获取板块信息
    home_page_text_title = (By.CLASS_NAME, "ts")  # 获取帖子题目
    home_page_text_huifu = (By.XPATH, "//div[@id='post_77']/table/tbody/tr/td[2]/div[2]/div/div/table/tbody")  # 获取回复内容
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
        self.click(*self.home_page_button_Submission)  # 发表回复

    def submit(self):
        self.driver.switch_to.window(self.driver.window_handles[2])
        self.click(*self.home_page_get_subject)
        m = self.driver.find_element_by_css_selector(".ts span")
        return m.text

    # 用户名，帖子题目，回帖信息，版块信息
    def find_id(self):
        # a=self.find_element(self.home_page_text_yonghu)
        a = self.driver.find_element_by_css_selector(".vwmy a")
        return a.text

    def find_title(self):
        # self.find_element(self.home_page_text_title)
        a = self.driver.find_element_by_css_selector(".ts").text
        return a

    def find_bankuai(self):
        # self.find_element(self.home_page_text_bankuai)
        a = self.driver.find_element_by_xpath("//div[@id='pt']/div/a[4]").text
        return a

    def find_huitie(self):
        a = self.driver.find_element_by_xpath(
            "//div[@id='postlistreply']/div/table/tbody/tr/td[2]/div[2]/div/div/table/tbody").text
        return a
