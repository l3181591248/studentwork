# 用户登录
# 进行帖子搜索
# 搜索haotest帖子
# 进入搜索的帖子
# 验证帖子标题和期望的一致
# 用户退出
import time
import unittest

from pageobjects.Basics_test import BasicsTestCase
from pageobjects.luntan_tiezi_page import Homepage


# @ddt
class ostSerch(BasicsTestCase):
    # @data(['haotest'])
    # @unpack
    def test_search(self):
        con_page=Homepage(self.driver)
        con_page.log_in("http://127.0.0.1/forum.php")
        con_page.login("l3181591248","030201")
        time.sleep(1)
        id = "l3181591248"
        expect = con_page.find_id()
        self.assertEqual(id, expect, msg=id)
        con_page.search("haotest")
        time.sleep(1)
        con_page.activation_window(1)
        con_page.search_result()
        time.sleep(1)
        con_page.activation_window(2)
        time.sleep(1)
        # con_page.submit()  #判断是否一致
        result = con_page.submit()
        expect=("haotest")
        self.assertEqual(result, expect, msg=result)
        con_page.Logout()
if __name__=="__main__":
    runner = unittest.TextTestRunner(verbosity=22)
    unittest.main()