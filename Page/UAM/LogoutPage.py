from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from getpass import getpass
import time

class LogoutPage:
    def __init__(self,driver):
        self.driver = driver
        self.driver = driver
        # self.profile_xpath = '//button/span/div/div/img[@class="navbar-avatar"]'
        self.profile_xpath = '//button/span/div/div/app-background-image/div'
        self.logoutButton_xpath = "//button/span[text()='Logout']"
        self.confirmButton_xpath = "//button/span[text()=' Confirm ']"

    def click_profile(self):
        self.driver.find_element_by_xpath(self.profile_xpath).click()
    def click_Logout(self):
        time.sleep(3)
        self.driver.find_element_by_xpath(self.logoutButton_xpath).click()
        time.sleep(2)
    def click_Confirm(self):
        self.driver.find_element_by_xpath(self.confirmButton_xpath).click()
        print("logout")


    def logout(self):
        self.click_profile()
        self.click_Logout()
        self.click_Confirm()

