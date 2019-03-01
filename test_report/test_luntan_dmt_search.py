import time
from pageobjects.Basics_test import BasicsTestCase
from pageobjects.luntan_Administrators_page import Homepage
import unittest

class ControllerSerch(BasicsTestCase):
    def test_contorller(self):
        con_page=Homepage(self.driver)
        con_page.log_in("http://127.0.0.1/forum.php")
        con_page.login("admin","030201")
        time.sleep(1)
        con_page.Default_block() #进入默认版块
        time.sleep(1)
        # if con_page.home_page_button_delet_choice is True:
        con_page.delet_choice() #删除
        # else:
        time.sleep(1)
        con_page.administration_center() #管理中心
        time.sleep(1)
        con_page.activation_window(1)
            # a=con_page.find(con_page.home_page_input_zhanghao)
            # print(a)
            # if con_page.home_page_input_zhanghao is None:
            #     pass
            # else:
            # con_page.userpwd("030201")
            # con_page.refer()
        con_page.luntan()
        con_page.ifram("main")
        con_page.xinbankuai()
        con_page.refer()
        con_page.ifram(self.driver.switch_to.parent_frame())
        con_page.Logout()  #新版块添加完毕
    def user_log(self):
        con_page = Homepage(self.driver)
        con_page.login("l3181591248","030201")
        time.sleep(1)
        con_page.goin_xinbankuai()
        con_page.title("english")
        con_page.content("嘤嘤嘤666666")
        con_page.Submission()  # 提交
        # 回帖
        con_page.content("楼主6666666666")
        time.sleep(15)
        con_page.Submission()
        time.sleep(1)
        con_page.Logout()

if __name__=="__main__":
    runner = unittest.TextTestRunner(ValueError=2)
    unittest.main()