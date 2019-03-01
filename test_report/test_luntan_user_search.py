import unittest
from pageobjects.Basics_test import BasicsTestCase
from pageobjects.luntan_user_page import Homepage
import time

class UserSearch(BasicsTestCase):

    def test_user_search(self):
        #声明homepage类对象
        home_page=Homepage(self.driver)

        home_page.log_in("http://127.0.0.1/forum.php")
        #调用首页搜索功能
        home_page.login("l3181591248","030201")
        time.sleep(1)
        home_page.Default_block()  #默认版块
        time.sleep(1)
        #发帖
        home_page.title("english")
        home_page.content("嘤嘤嘤666666")
        home_page.Submission()#提交
        #回帖
        home_page.content("楼主6666666666")
        time.sleep(15)
        home_page.Submission()
        time.sleep(1)
        home_page.Logout()

if __name__=="__main__":
    runner = unittest.TextTestRunner(verbosity=2)
    unittest.main()