import unittest

from framwork.browser_engine import BrowserEngin


class BasicsTestCase(unittest.TestCase):
    def setUp(self):
        browser = BrowserEngin()
        self.driver = browser.open_browser()
        # self.driver=webdriver.Chrome("../tools/chromedriver.exe")
        # self.driver.implicitly_wait(6)
        # self.driver.maximize_window()

    def send_url(self):
        url = self.driver.current_url
        return url
    def tearDown(self):
        print("完成")
        self.driver.quit()