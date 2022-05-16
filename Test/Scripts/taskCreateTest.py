import unittest
from selenium import webdriver
import time
from Page.UAM.LoginPage import LoginPage
from Page.TaskCreate.TaskCreate import TaskCreate
from TestBase.WebDriverSetup import WebDriverSetup


class TestTaskCreate(WebDriverSetup):
    def test_customertaskcreate_success(self):
        driver = self.driver
        base_URL = "https://stage-ontrex.selise.biz/"
        taskId = "company/32645f76-7d70-418f-965a-40f897c1edef/545c3345-62a7-4dc5-ac76-59bb320294aa/package-request/package-list"
        driver.get(base_URL + taskId)

        '""""""""Driver initialize """"'
        Login_page = LoginPage(driver)
        Task_Create = TaskCreate(driver)
        time.sleep(5)
        Login_page.login("qarstage_invuser@yopmail.com", "1qazZAQ!")
        time.sleep(5)

        try:
            assert "Package-list < Package-request < Company | Ontrex SPA Portal"== driver.title
        except Exception as e:
            raise
            print("Title is wrong", format(e))


        PackageName = "input(""Enter Package Name--- >"")"
        Contract = "Mail Test"
        #Contract = input("Enter Contract Name--- >")
        SLA = "FLAT Rate"
        #SLA = input("Enter SLA Name--- >")
        PackageTechnology = "MacOS"
        OsDef = "Stage Customer OS, QAR_Windows10, QAR_SP1 , ENG"
        UploadFile = "C:\\Users\\ahasanul.rifat\\Desktop\\Testing\\sample.zip"
        CostCenter = "Test cost center V 0.3.18"
        Task_Create.customer_packagereq(PackageName,"Auto Create",Contract,SLA, "QA Selise","QAR Invite User STG",PackageTechnology,OsDef,UploadFile,CostCenter )

