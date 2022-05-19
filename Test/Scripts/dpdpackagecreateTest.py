import unittest
from selenium import webdriver
import time
from Page.UAM.LoginPage import LoginPage
from Page.TaskCreate.DpdPackageCreate import DpdPackage
from TestBase.WebDriverSetup import WebDriverSetup


class TestTaskCreate(WebDriverSetup):
    # def test_dpdpackagecreate_success(self):
    #     driver = self.driver
    #     base_URL = "https://stage-ontrex.selise.biz/"
    #     taskId = "task-management/task-list"
    #     driver.get(base_URL + taskId)
    #
    #     '""""""""Driver initialize """"'
    #     Login_page = LoginPage(driver)
    #     Dpd_Package = DpdPackage(driver)
    #     time.sleep(5)
    #     Login_page.login("superadmin@ontrex.ch", "2wsxXSW@")
    #     time.sleep(5)
    #
    #     # try:
    #     #     assert "Package-list < Package-request < Company | Ontrex SPA Portal"== driver.title
    #     # except Exception as e:
    #     #     raise
    #     #     print("Title is wrong", format(e))
    #
    #     ProductName ="DPD test 19.05.2022"
    #     PackageName = "Auto DPD PAck Create OTX Admin - 19/05/2022-- 01"
    #     Contract = "Ontrex DPD"
    #     #Contract = input("Enter Contract Name--- >")
    #     SLA = "Security Relevant Product"
    #     #SLA = input("Enter SLA Name--- >")
    #     PackageTechnology = "MacOS"
    #     OsDef = "Stage Customer OS, QAR_Windows10, QAR_SP1 , ENG"
    #     UploadFile = "C:\\Users\\ahasanul.rifat\\Desktop\\Testing\\sample.zip"
    #     CostCenter = "Test cost center V 0.3.18"
    #     Dpd_Package.dpd_packageCreate(ProductName,PackageName,"Auto Create By OTX Admin",Contract,SLA, "QA Selise",PackageTechnology,OsDef,UploadFile )

    def test_dpdsupersedepackage(self):
        driver = self.driver
        base_URL = "https://stage-ontrex.selise.biz/"
        taskId = "task-management/task-list"
        driver.get(base_URL + taskId)

        '""""""""Driver initialize """"'
        Login_page = LoginPage(driver)
        Dpd_Package = DpdPackage(driver)
        time.sleep(5)
        Login_page.login("superadmin@ontrex.ch", "2wsxXSW@")
        time.sleep(5)

        # try:
        #     assert "Package-list < Package-request < Company | Ontrex SPA Portal"== driver.title
        # except Exception as e:
        #     raise
        #     print("Title is wrong", format(e))

        ProductName ="DPD test 19.05.2022"
        SelectPackageName = "Auto DPD PAck Create OTX Admin - 19/05/2022-- 01"
        PackageName = "Auto DPD PAck Create OTX Admin - 19/05/2022-- 01"
        Contract = "Ontrex DPD"
        #Contract = input("Enter Contract Name--- >")
        SLA = "Security Relevant Product"
        #SLA = input("Enter SLA Name--- >")
        PackageTechnology = "MacOS"
        OsDef = "Stage Customer OS, QAR_Windows10, QAR_SP1 , ENG"
        UploadFile = "C:\\Users\\ahasanul.rifat\\Desktop\\Testing\\sample.zip"
        Dpd_Package.dpd_supersedepackagecreate(ProductName,SelectPackageName,PackageName,"Auto Create By OTX Admin",Contract,SLA, "QA Selise",PackageTechnology,OsDef,UploadFile)

