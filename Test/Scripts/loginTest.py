import unittest
from selenium import webdriver
import time
import sys
sys.path.append("C:/Users/ahasanul.rifat/PycharmProjects/OntrexWithReport")
##Use for avoiding create path in windows advance path setting

from Page.UAM.LoginPage import LoginPage
from TestBase.WebDriverSetup import WebDriverSetup




class TestLogin(WebDriverSetup):

    def test_login_success(self):
        driver = self.driver
        driver.get("https://stage-ontrex.selise.biz/")
        Login_page = LoginPage(driver)
        # Login_page.username("superadmin@ontrex.ch")
        # Login_page.password("1qazZAQ!")
        # Login_page.submit()

        Login_page.login("superadmin@ontrex.ch","2wsxXSW@")
        time.sleep(10)

        try:
            assert "Landing | Ontrex SPA Portal" == driver.title
        except Exception as e:
            raise
            print("Title is wrong", format(e))
#
if __name__ =='__main__':
    unittest.main()

#
# """"For Generate Reports"""
# OntrexWithReport\Test\Scripts>python login_test.py
