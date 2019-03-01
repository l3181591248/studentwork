from framwork.browser_engine import BrowserEngin
import unittest
from selenium import webdriver

class BasicsTestCase(unittest.TestCase):
    def setUp(self):
        browser = BrowserEngin()
        self.driver = browser.open_browser()
        # self.driver=webdriver.Chrome("../tools/chromedriver.exe")
        # self.driver.implicitly_wait(6)
        # self.driver.maximize_window()
    def tearDown(self):
        print("完成")
        self.driver.quit()