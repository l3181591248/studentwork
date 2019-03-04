import time
import unittest

from pageobjects.Basics_test import BasicsTestCase
from pageobjects.luntan_Administrators_page import Homepage


class ControllerSerch(BasicsTestCase):
    def test_contorller(self):
        con_page=Homepage(self.driver)
        con_page.log_in("http://127.0.0.1/forum.php")
        con_page.login("admin","030201")
        time.sleep(1)
        id = "admin"
        expect = con_page.find_id()
        self.assertEqual(id, expect, msg=id)
        con_page.Default_block() #进入默认版块
        time.sleep(1)
        expect = con_page.find_bankuai()
        bankuai = "默认版块"
        self.assertEqual(bankuai, expect, msg=bankuai)
        con_page.delet_choice() #删除
        # else:
        time.sleep(1)
        con_page.administration_center() #管理中心
        time.sleep(1)
        con_page.activation_window(1)
        zhongxin_id = con_page.find_zhongxin_id()
            # a=con_page.find(con_page.home_page_input_zhanghao)
        # print(a)
        if zhongxin_id is None:
            pass
        else:
            con_page.pwd("030201")
            con_page.refer()
        time.sleep(1)
        title = "Discuz! Board 管理中心 - 首页"
        content = con_page.find_zhongxin()
        self.assertEqual(title, content, msg=title)
        con_page.luntan()
        con_page.ifram("main")
        con_page.xinbankuai()
        con_page.refer()
        con_page.ifram(self.driver.switch_to.parent_frame())
        con_page.Logout()  #新版块添加完毕
        con_page.Logout()
        con_page.login("l3181591248","030201")
        time.sleep(1)
        id = "l3181591248"
        expect = con_page.find_id()
        self.assertEqual(id, expect, msg=id)
        con_page.goin_xinbankuai()
        expect = con_page.find_bankuai()
        bankuai = "新版块名称"
        self.assertEqual(bankuai, expect, msg=bankuai)
        con_page.fatie_title("english")
        con_page.content("嘤嘤嘤666666")
        con_page.Submission()  # 提交
        # 回帖
        con_page.content("楼主6666666666")
        time.sleep(15)
        con_page.Submission()
        title = con_page.find_title()
        expect = ("english")
        self.assertEqual(title, expect, msg=title)
        content = con_page.find_huitie()
        expect = ("楼主6666666666")
        self.assertEqual(content, expect, msg=content)
        time.sleep(1)
        con_page.Logout()

if __name__=="__main__":
    runner = unittest.TextTestRunner(verbosity=2)
    unittest.main()