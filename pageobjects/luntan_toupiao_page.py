from selenium.webdriver.common.by import By
from  framwork.Basics import Basic
import time

class Homepage(Basic):
    home_page_input_username = (By.ID, "ls_username")  # 用户名
    home_page_input_pwd = (By.XPATH, "//input[@type='password']")  # 密码
    home_page_button_Default_block = (By.CSS_SELECTOR, ".fl_tb a")  # 默认版块
    home_page_button_vote = (By.ID, "newspecial")  # 发帖
    home_page_button_vote_an = (By.PARTIAL_LINK_TEXT, "发起投票")  #(进入投票界面)
    home_page_input_search3_loc = (By.NAME, 'subject')  # 投票标题
    home_page_input_vote_option1 = (By.CSS_SELECTOR, '.mbm p:nth-child(1) input')  # 投票选项
    home_page_input_vote_option2 = (By.CSS_SELECTOR, '.mbm p:nth-child(2) input')  # 投票选项
    home_page_input_vote_option3 = (By.CSS_SELECTOR, '.mbm p:nth-child(3) input')  # 投票选项
    home_page_input_vote_content = (By.XPATH, "//body[@spellcheck='false']")  # 投票内容
    home_page_button_search2_loc = (By.NAME, 'topicsubmit')  # 发起投票
    home_page_button_login = (By.CSS_SELECTOR, ".fastlg_l button")  # 登录
    home_page_button_quit=(By.LINK_TEXT,"退出")
    #search_loc   是投票选项的内容
    #search_fen    是百分比
    home_page_label_search1_loc=(By.XPATH,"//form[@id='poll']/div[2]/table/tbody/tr/td[1]/label")
    home_page_label_search2_loc = (By.XPATH, "// form[ @ id = 'poll'] / div[2] / table / tbody / tr[3] / td[1] / label")
    home_page_label_search3_loc = (By.XPATH, "//form[@id='poll']/div[2]/table/tbody/tr[5]/td[1]/label")
    home_page_button_fen1_loc=(By.XPATH,"//form[@id='poll']/div[2]/table/tbody/tr[2]/td[2]")
    home_page_button_fen2_loc = (By.XPATH, "//form[@id='poll']/div[2]/table/tbody/tr[4]/td[2]")
    home_page_button_fen3_loc = (By.XPATH, "//form[@id='poll']/div[2]/table/tbody/tr[6]/td[2]")
    home_page_button_toupiao=(By.XPATH,"//form[@id='poll']/div[2]/table/tbody/tr[7]/td[2]/button")
    home_page_button_xuanze1=(By.XPATH,"//form[@id='poll']/div[2]/table/tbody/tr[5]/td[1]")




    def vote(self):
        time.sleep(1)
        self.click(*self.home_page_button_Default_block)  # 点击默认版块
        time.sleep(1)
        self.click(*self.home_page_button_vote)  #投票
        time.sleep(1)
        self.click(*self.home_page_button_vote_an)

    def vote_option(self,content1,content2,content3):
        self.sendkeys(content1,*self.home_page_input_vote_option1)#1,2,3   投票选项的内容
        self.sendkeys(content2, *self.home_page_input_vote_option2)
        self.sendkeys(content3, *self.home_page_input_vote_option3)
    def vote_content(self,content):
        self.sendkeys(content,*self.home_page_input_vote_content) #投票内容
    def tijiaotoupiao(self):
        self.click(*self.home_page_button_search2_loc)
    def ifram(self,m):
        self.driver.switch_to.frame(m)
    def login(self,name,pwd):
        self.sendkeys(name, *self.home_page_input_username)  # 用户名
        self.sendkeys(pwd, *self.home_page_input_pwd)  # 密码
        self.click(*self.home_page_button_login)#登录
    def tijiao(self):
        self.click(*self.home_page_button_xuanze1)
        self.click(*self.home_page_button_toupiao)
    def Logout(self):
        self.click(*self.home_page_button_quit)#退出登录
    def vote_title(self,content):
        self.sendkeys(content, *self.home_page_input_search3_loc)
    def display(self):
        self.text(*self.home_page_label_search1_loc)
        self.text(*self.home_page_label_search2_loc)
        self.text(*self.home_page_label_search3_loc)
        self.text(*self.home_page_button_fen1_loc)
        self.text(*self.home_page_button_fen2_loc)
        self.text(*self.home_page_button_fen3_loc)