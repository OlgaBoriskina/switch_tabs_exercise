from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

import test
import authorization
import unittest

base_url = "http://way2automation.com/way2auto_jquery"
frame_locator = "//iframe[@src='droppable/default.html']"


class Test (unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome("chromedriver.exe")
        self.driver.get(base_url)
        self.wait = WebDriverWait(self.driver, 10)
        authorization.authorize(self.wait)
        self.driver.refresh()
        self.driver.get(base_url + "/frames-and-windows.php")

    def test_switch_tabs(self):
        assert (len(test.switch_tabs(self.driver,self.wait)) > 0)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()