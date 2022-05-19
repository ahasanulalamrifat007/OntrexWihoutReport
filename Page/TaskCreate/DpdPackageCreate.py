from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from getpass import getpass
import time

class DpdPackage:
    def __init__(self, driver):
        self.driver = driver
        self.newTask_xpath = "//button/span/span[text()='New Task']"
        self.dpdPackage_xpath = "//table/tr/td/p[text()='New Package']"  #DPD Package from Admin
        self.supersedepackage_xpath = "//table/tr/td/p[text()='Supersede Package']"
        self.selectPackage_xpath = '//mat-select[@aria-label="Select Package"]'
        self.addButton_xpath = "//button/span[text()=' Add ']"
        self.selectProduct_xpath = '//input[@placeholder="Search by product name"]'
        self.superselectProduct_xpath = '//mat-select[@aria-label="Select Product"]'
        # self.dpdProduct_xpath = '//input[@placeholder="Search by product name"]'
        self.packageName_xpath = "//input[@placeholder='Package Name']"
        self.packageDescription_xpath = "//textarea[@placeholder='Package Description']"
        self.contract_xpath = "//mat-select[@formcontrolname='CONTRACT']"
        self.sla_xpath = "//mat-select[@formcontrolname='SLA']"
        self.customerRef_xpath = '//input[@formcontrolname="CustomerReference"]'
        self.contactPerson_xpath = "//mat-select[@formcontrolname='ContactPerson']"
        self.packageTechnology_xpath = "//mat-select[@formcontrolname='PACKAGETECHNOLOGY']"
        self.osDef_xpath = "//mat-select[@formcontrolname='OSDEFINATION']"
        self.uploadfile_xpath = "//input[@type='file']"
        self.costCenter_xpath = "//mat-select[@formcontrolname='CostCenter']"
        self.priority_id = "mat-radio-9"
        self.updatePriority_id = "mat-radio-7"
        self.complexity_id = "mat-radio-13"
        self.updateComplexity_id = "mat-radio-11"
        self.versionNumber = '//input[@placeholder="Version Number"]'
        self.confirmButton_xpath = "//button/span[text()=' Confirm ']"
        self.okButton_xpath = "//button/span[text()='OK']"
    def click_MakePackageReq(self):
        time.sleep(5)
        self.driver.find_element_by_xpath(self.makePackageReq_xpath).click()
        # from customer

    def click_NewTask(self):
        time.sleep(5)
        self.driver.find_element_by_xpath(self.newTask_xpath).click()
    def click_NewDPDPackage(self):
        time.sleep(5)
        self.driver.find_element_by_xpath(self.dpdPackage_xpath).click()
        #DPD Package from Admin
    def click_SuperSedePackage(self):
        time.sleep(5)
        self.driver.find_element_by_xpath(self.supersedepackage_xpath).click()
        # DPD Package new version update from Admin

    '""""""""Update for""""'

    def enter_SelectProduct(self, SelectProduct):
        time.sleep(2)
        self.driver.find_element_by_xpath(self.selectProduct_xpath).send_keys(SelectProduct)
        time.sleep(5)
        self.driver.find_element_by_xpath(self.selectProduct_xpath).send_keys(Keys.ARROW_DOWN)
        self.driver.find_element_by_xpath(self.selectProduct_xpath).send_keys(Keys.ENTER)
        self.driver.find_element_by_xpath(self.selectProduct_xpath).send_keys(Keys.TAB)

    def enter_SuperSelectProduct(self, SelectProduct):
        time.sleep(2)
        self.driver.find_element_by_xpath(self.superselectProduct_xpath).send_keys(SelectProduct)
        # time.sleep(5)
        # self.driver.find_element_by_xpath(self.superselectProduct_xpath).send_keys(Keys.ARROW_DOWN)
        # self.driver.find_element_by_xpath(self.superselectProduct_xpath).send_keys(Keys.ENTER)
        # self.driver.find_element_by_xpath(self.superselectProduct_xpath).send_keys(Keys.TAB)

    def enter_SelectPackage(self, SelectPackage):
        time.sleep(2)
        self.driver.find_element_by_xpath(self.selectPackage_xpath).send_keys(SelectPackage)
        time.sleep(5)
        self.driver.find_element_by_xpath(self.selectPackage_xpath).send_keys(Keys.ARROW_DOWN)
        self.driver.find_element_by_xpath(self.selectPackage_xpath).send_keys(Keys.ENTER)
        self.driver.find_element_by_xpath(self.selectPackage_xpath).send_keys(Keys.TAB)
    def enter_SuperSelectPackage(self, SelectPackage):
        time.sleep(2)
        self.driver.find_element_by_xpath(self.selectPackage_xpath).send_keys(SelectPackage)
        # time.sleep(5)
        # self.driver.find_element_by_xpath(self.selectPackage_xpath).send_keys(Keys.ARROW_DOWN)
        # self.driver.find_element_by_xpath(self.selectPackage_xpath).send_keys(Keys.ENTER)
        # self.driver.find_element_by_xpath(self.selectPackage_xpath).send_keys(Keys.TAB)


    '""""""""Custom package """"'
    def click_CustomPackage(self):
        time.sleep(5)
        self.driver.find_element_by_xpath(self.customPackage_xpath).click()

    def enter_DPDProduct(self, DPDProduct):
        time.sleep(2)
        self.driver.find_element_by_xpath(self.dpdProduct_xpath).send_keys(DPDProduct)
        time.sleep(5)
        self.driver.find_element_by_xpath(self.dpdProduct_xpath).send_keys(Keys.ARROW_DOWN)
        self.driver.find_element_by_xpath(self.dpdProduct_xpath).send_keys(Keys.ENTER)
        self.driver.find_element_by_xpath(self.dpdProduct_xpath).send_keys(Keys.TAB)
        print("Customer select successfull")
    def click_ADD(self):
        self.driver.find_element_by_xpath(self.addButton_xpath).click()
    def enter_PackageName(self, PackageName):
        self.driver.find_element_by_xpath(self.packageName_xpath).send_keys(PackageName)
    def enter_PackageDescription(self, PackageDescription):
        self.driver.find_element_by_xpath(self.packageDescription_xpath).send_keys(PackageDescription)
    def enter_Contract(self, Contract):
        self.driver.find_element_by_xpath(self.contract_xpath).send_keys(Contract)
        time.sleep(5)
        self.driver.find_element_by_xpath(self.contract_xpath).send_keys(Keys.ARROW_DOWN)
        self.driver.find_element_by_xpath(self.contract_xpath).send_keys(Keys.ENTER)
        self.driver.find_element_by_xpath(self.contract_xpath).send_keys(Keys.TAB)
        print("Contract select successfull")
    def enter_SLA(self, SLA):
        time.sleep(5)
        self.driver.find_element_by_xpath(self.sla_xpath).send_keys(SLA)
        time.sleep(10)
        # PLEASE ADD IF ELSE CONDITION
        self.driver.find_element_by_xpath(self.sla_xpath).send_keys(Keys.ARROW_DOWN)
        self.driver.find_element_by_xpath(self.sla_xpath).send_keys(Keys.ENTER)
        self.driver.find_element_by_xpath(self.sla_xpath).send_keys(Keys.TAB)
        print("SLA select successfull")
    def enter_CustomerRef(self, CustomerRef):
        self.driver.find_element_by_xpath(self.customerRef_xpath).send_keys(CustomerRef)
        time.sleep(2)

    def enter_PackageTechnology(self, PackageTechnology):
        self.driver.find_element_by_xpath(self.packageTechnology_xpath).send_keys(PackageTechnology)
        time.sleep(5)
        self.driver.find_element_by_xpath(self.packageTechnology_xpath).send_keys(Keys.ARROW_DOWN)
        self.driver.find_element_by_xpath(self.packageTechnology_xpath).send_keys(Keys.ENTER)
        self.driver.find_element_by_xpath(self.packageTechnology_xpath).send_keys(Keys.TAB)
    def enter_OsDef(self, OsDef):
        self.driver.find_element_by_xpath(self.osDef_xpath).send_keys(OsDef)
        time.sleep(5)
        self.driver.find_element_by_xpath(self.osDef_xpath).send_keys(Keys.ARROW_DOWN)
        self.driver.find_element_by_xpath(self.osDef_xpath).send_keys(Keys.ENTER)
        self.driver.find_element_by_xpath(self.osDef_xpath).send_keys(Keys.TAB)
    def enter_UploadFile(self, UploadFile):
        self.driver.find_element_by_xpath(self.uploadfile_xpath).send_keys(UploadFile)

    def click_Priority(self):
        time.sleep(2)
        self.driver.find_element_by_id(self.priority_id).click()
        # self.driver.find_element_by_xpath(self.priority_xpath).click()

    def click_Complexity(self):
        time.sleep(2)
        self.driver.find_element_by_id(self.complexity_id).click()
        # self.driver.find_element_by_id(self.complexity_id).click()
        # self.driver.find_element_by_xpath(self.complexity_xpath).click()

    def click_UpdatePriority(self):
        self.driver.find_element_by_id(self.updatePriority_id).click()

    def click_UpdateComplexity(self):
        self.driver.find_element_by_id(self.updateComplexity_id).click()
    def enter_VersionNum(self, VersionNum):
        self.driver.find_element_by_xpath(self.versionNumber).send_keys(VersionNum)
    def click_Confirm(self):
        self.driver.find_element_by_xpath(self.confirmButton_xpath).click()
        time.sleep(5)
    def click_OkButton(self):
        self.driver.find_element_by_xpath(self.okButton_xpath).click()
        print("Custom Package Done")

    def dpd_packageCreate(self,ProductName,PackageName,PackageDescription,Contract,SLA,CustomerRef,PackageTechnology,OsDef,UploadFile):
        self.click_NewTask()
        time.sleep(5)
        self.click_NewDPDPackage()
        time.sleep(5)
        self. enter_SelectProduct(ProductName)
        time.sleep(5)
        self.click_ADD()
        time.sleep(3)
        self.enter_PackageName(PackageName)
        time.sleep(3)
        self.enter_PackageDescription(PackageDescription)
        time.sleep(3)
        self.enter_Contract(Contract)
        time.sleep(5)
        self.enter_SLA(SLA)
        time.sleep(5)
        self.enter_CustomerRef(CustomerRef)
        time.sleep(3)
        self.enter_PackageTechnology(PackageTechnology)
        time.sleep(3)
        self.enter_OsDef(OsDef)
        time.sleep(3)
        self.enter_UploadFile(UploadFile)
        time.sleep(5)
        self.click_Priority()
        time.sleep(3)
        self.click_Complexity()
        time.sleep(5)
        self.click_Confirm()
        time.sleep(5)
        self.click_OkButton()

    def dpd_supersedepackagecreate(self,ProductName,SelectPackageName,PackageName,PackageDescription,Contract,SLA,CustomerRef,PackageTechnology,OsDef,UploadFile):
        self.click_NewTask()
        time.sleep(5)
        self.click_SuperSedePackage()
        time.sleep(5)
        self. enter_SuperSelectProduct(ProductName)
        time.sleep(5)
        self. enter_SuperSelectPackage(SelectPackageName)
        time.sleep(5)
        self.click_ADD()
        time.sleep(3)
        self.enter_PackageName(PackageName)
        time.sleep(3)
        self.enter_PackageDescription(PackageDescription)
        time.sleep(3)
        self.enter_Contract(Contract)
        time.sleep(5)
        self.enter_SLA(SLA)
        time.sleep(5)
        self.enter_CustomerRef(CustomerRef)
        time.sleep(3)
        self.enter_PackageTechnology(PackageTechnology)
        time.sleep(3)
        self.enter_OsDef(OsDef)
        time.sleep(3)
        self.enter_UploadFile(UploadFile)
        time.sleep(5)
        self.click_Priority()
        time.sleep(3)
        self.click_Complexity()
        time.sleep(5)
        self.click_Confirm()
        time.sleep(5)
        self.click_OkButton()
