import unittest
from pageobjects.baidu_homepage import Homepage
from pageobjects.Basics_test import BasicsTestCase

class BaiduSearch(BasicsTestCase):

    def test_baidu_search(self):
        #声明homepage类对象
        home_page=Homepage(self.driver)

        home_page.log_in("https://www.baidu.com")
        #调用首页搜索功能
        home_page.search("selenium")
        # home_page.get_windows_img()


if __name__=="__main__":
    runner = unittest.TextTestRunner(verbosity=2)
    unittest.main()