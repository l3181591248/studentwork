# 发表投票帖子
# 进行投票
# 取出投票各个选项的名称以及投票比例
# 取出投票的主题名称

import time
from pageobjects.Basics_test import BasicsTestCase
from pageobjects.luntan_toupiao_page import Homepage
import unittest

class OstSerch(BasicsTestCase):
    def test_contorller(self):
        con_page=Homepage(self.driver)
        con_page.log_in("http://127.0.0.1/forum.php")
        con_page.login("l3181591248","030201")
        con_page.vote()
        con_page.vote_title("管理最帅")
        time.sleep(1)
        con_page.vote_option("嘤1","嘤2","嘤3")
        con_page.ifram("e_iframe")
        con_page.vote_content("嘤内容")
        con_page.ifram(self.driver.switch_to.parent_frame())
        con_page.tijiaotoupiao()
        con_page.tijiao()
        con_page.display()

if __name__=="__main__":
    runner = unittest.TextTestRunner(ValueError=2)
    unittest.main()