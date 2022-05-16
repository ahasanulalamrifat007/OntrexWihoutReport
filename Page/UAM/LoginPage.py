from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from getpass import getpass
import time

class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.username_id = "mat-input-0"
        self.password_id = "mat-input-1"
        self.loginbutton_xpath = "//*[@id='login-form']/form/button"


    def username(self, UserName):
        self.driver.find_element_by_id(self.username_id).clear()
        self.driver.find_element_by_id(self.username_id).send_keys(UserName)

    def password(self,PassWord):
        self.driver.find_element_by_id(self.password_id).clear()
        self.driver.find_element_by_id(self.password_id).send_keys(PassWord)
    def submit(self):
        self.driver.find_element_by_xpath(self.loginbutton_xpath).click()
        time.sleep(5)
        print("Login Successful")
    def login(self, UserName, PassWord):
        self.username(UserName)
        self.password(PassWord)
        self.submit()














