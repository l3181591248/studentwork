from selenium.webdriver.common.by import By
from framwork.Basics import Basic

class Homepage(Basic):
    #定位器，通过元素属性定位元素位置
    home_page_input_search_loc=(By.ID,"kw")
    home_page_button_search_loc = (By.ID, "su")
    #输入搜索内容并提交
    def search(self,content):
        self.sendkeys(content,*self.home_page_input_search_loc)
        self.click(*self.home_page_button_search_loc)

