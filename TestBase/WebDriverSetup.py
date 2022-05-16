import unittest
from selenium import webdriver
import time
from time import sleep
import urllib3



class WebDriverSetup(unittest.TestCase):
    @classmethod
    def setUp(self):
        print("Initiating Chrome driver")
        self.driver = webdriver.Chrome(executable_path="C:\webdrivers\chromedriver_win32 (1)\chromedriver.exe")
        print("-----------------------------------------")
        print("Test is started")
        self.driver.implicitly_wait(10)
        # self.driver.get("http://ontrex.seliselocal.com/login")
        self.driver.maximize_window()

    # @classmethod
    # def tearDown(self):
    #     if (self.driver != None):
    #         print("Cleanup of test environment")
    #         self.driver.close()
    #         self.driver.quit()