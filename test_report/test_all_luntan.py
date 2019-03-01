from test_report import test_ost_search
from test_report import test_vote
from test_report import test_luntan_dmt_search
from test_report import test_luntan_user_search
import selenium
import time
import os
import unittest

test1=unittest.TestLoader().loadTestsFromTestCase(test_luntan_user_search.UserSearch)
test2=unittest.TestLoader().loadTestsFromTestCase(test_luntan_dmt_search.ControllerSerch)
test3=unittest.TestLoader().loadTestsFromTestCase(test_ost_search.ostSerch)
test4=unittest.TestLoader().loadTestsFromTestCase(test_vote.OstSerch)

test_all_1=unittest.TestSuite([test1,test2])
test_all_2=unittest.TestSuite([test3,test4])
unittest.TextTestRunner(verbosity=2).run(test_all_1)
time.sleep(1)
unittest.TextTestRunner(verbosity=2).run(test_all_2)