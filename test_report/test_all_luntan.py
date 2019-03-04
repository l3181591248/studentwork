import os
import unittest

import HTMLTestRunner
from test_report import test_luntan_dmt_search
from test_report import test_luntan_user_search
from test_report import test_ost_search
from test_report import test_vote


test1=unittest.TestLoader().loadTestsFromTestCase(test_luntan_user_search.UserSearch)
test2=unittest.TestLoader().loadTestsFromTestCase(test_luntan_dmt_search.ControllerSerch)
test3=unittest.TestLoader().loadTestsFromTestCase(test_ost_search.ostSerch)
test4=unittest.TestLoader().loadTestsFromTestCase(test_vote.OstSerch)

test_all=unittest.TestSuite([test1,test2,test3,test4])
# test_all_2=unittest.TestSuite([test3,test4])
# unittest.TextTestRunner(verbosity=2).run(test_all)
# unittest.TextTestRunner(verbosity=2).run(test_all_2)

cur_path = os.path.dirname((os.path.realpath(__file__)))
test_result = os.path.join(cur_path, "report")
if not os.path.exists(test_result): os.mkdir(test_result)
if __name__ == "__main__":
    # suit = unittest.TestSuite()
    # suit.addTest(unittest.makeSuite(test_luntan_user_search))
    # suit.addTest(unittest.makeSuite(test_luntan_dmt_search))
    # suit.addTest(unittest.makeSuite(test_ost_search))
    # suit.addTest(unittest.makeSuite(test_vote))
    html_report = test_result + r"/restlt.html"
    fp = open(html_report, "wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, verbosity=2, title="测试报告", description="测试报告")
    runner.run(test_all)
    fp.close()
