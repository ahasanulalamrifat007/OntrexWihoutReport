from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from getpass import getpass
import time

class TaskCreate():
    def __init__(self,driver):
        self.driver = driver
        self.makePackageReq_xpath = "//button/span[text()=' MAKE PACKAGE REQUEST ']"  # from customer
        self.newTask_xpath = "//button/span/span[text()='New Task_Pages']"
        self.customPackage_xpath = "//table/tr/td/p[text()='Custom package']"
        self.dpdPackage_xpath = "//table/tr/td/p[text()='New Product']"  # DPD Package from Admin
        self.customer_xpath = "//mat-select/div/div/span[text()='Customer']"
        self.customerName_xpath = "//mat-option/span/ngx-mat-select-search/div/input"
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
        self.priority_id = "mat-radio-6"
        self.complexity_id = "mat-radio-10"
        # self.complexity_xpath = '//*[@id="mat-radio-10"]/label/div[1]/div[2]'
        self.confirmButton_xpath = "//button/span[text()=' Confirm ']"
        self.okButton_xpath = "//button/span[text()='OK']"

    def click_MakePackageReq(self):
        time.sleep(5)
        self.driver.find_element_by_xpath(self.makePackageReq_xpath).click()
        # from customer

    def click_NewDPDPackage(self):
        time.sleep(5)
        self.driver.find_element_by_xpath(self.dpdPackage_xpath).click()
        # DPD Package from Admin

    def click_NewTask(self):
        time.sleep(5)
        self.driver.find_element_by_xpath(self.newTask_xpath).click()

    def click_CustomPackage(self):
        time.sleep(5)
        self.driver.find_element_by_xpath(self.customPackage_xpath).click()

    def enter_Customers(self, Customers):
        self.driver.find_element_by_xpath(self.customer_xpath).click()
        time.sleep(2)
        self.driver.find_element_by_xpath(self.customerName_xpath).send_keys(Customers)
        time.sleep(5)
        self.driver.find_element_by_xpath(self.customerName_xpath).send_keys(Keys.ARROW_DOWN)
        self.driver.find_element_by_xpath(self.customerName_xpath).send_keys(Keys.ENTER)
        self.driver.find_element_by_xpath(self.customerName_xpath).send_keys(Keys.TAB)
        # print("Customer select successfull")

    def enter_PackageName(self, PackageName):
        self.driver.find_element_by_xpath(self.packageName_xpath).send_keys(PackageName)

    def enter_PackageDescription(self, PackageDescription):
        self.driver.find_element_by_xpath(self.packageDescription_xpath).send_keys(PackageDescription)

    def enter_Contract(self, Contract):
        time.sleep(2)
        self.driver.find_element_by_xpath(self.contract_xpath).send_keys(Contract)
        time.sleep(5)
        self.driver.find_element_by_xpath(self.contract_xpath).send_keys(Keys.ARROW_DOWN)
        self.driver.find_element_by_xpath(self.contract_xpath).send_keys(Keys.ENTER)
        self.driver.find_element_by_xpath(self.contract_xpath).send_keys(Keys.TAB)
        print("Contract select successfull")

    def enter_SLA(self, SLA):
        time.sleep(2)
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, self.sla_xpath))).send_keys(SLA)
            time.sleep(5)
            # PLEASE ADD IF ELSE CONDITION
            self.driver.find_element_by_xpath(self.sla_xpath).send_keys(Keys.ARROW_DOWN)
            time.sleep(5)
            self.driver.find_element_by_xpath(self.sla_xpath).send_keys(Keys.ENTER)
            self.driver.find_element_by_xpath(self.sla_xpath).send_keys(Keys.TAB)
            print("SLA select successfull")
        finally:
            print("Not Found")

    def enter_CustomerRef(self, CustomerRef):
        self.driver.find_element_by_xpath(self.customerRef_xpath).send_keys(CustomerRef)
        time.sleep(2)

    def enter_ContactPerson(self, ContactPerson):
        self.driver.find_element_by_xpath(self.contactPerson_xpath).send_keys(ContactPerson)
        time.sleep(5)
        # self.driver.find_element_by_xpath(self.contactPerson_xpath).send_keys(Keys.ARROW_DOWN)
        self.driver.find_element_by_xpath(self.contactPerson_xpath).send_keys(Keys.ENTER)
        self.driver.find_element_by_xpath(self.contactPerson_xpath).send_keys(Keys.TAB)

    def enter_PackageTechnology(self, PackageTechnology):
        self.driver.find_element_by_xpath(self.packageTechnology_xpath).send_keys(PackageTechnology)
        time.sleep(5)
        # self.driver.find_element_by_xpath(self.packageTechnology_xpath).send_keys(Keys.ARROW_DOWN)
        # self.driver.find_element_by_xpath(self.packageTechnology_xpath).send_keys(Keys.ENTER)
        # self.driver.find_element_by_xpath(self.packageTechnology_xpath).send_keys(Keys.TAB)

    def enter_OsDef(self, OsDef):
        self.driver.find_element_by_xpath(self.osDef_xpath).send_keys(OsDef)
        time.sleep(5)
        # self.driver.find_element_by_xpath(self.osDef_xpath).send_keys(Keys.ARROW_DOWN)
        # self.driver.find_element_by_xpath(self.osDef_xpath).send_keys(Keys.ENTER)
        self.driver.find_element_by_xpath(self.osDef_xpath).send_keys(Keys.TAB)

    def enter_UploadFile(self, UploadFile):
        self.driver.find_element_by_xpath(self.uploadfile_xpath).send_keys(UploadFile)

    def enter_CostCenter(self, CostCenter):
        self.driver.find_element_by_xpath(self.costCenter_xpath).send_keys(CostCenter)
        time.sleep(5)
        self.driver.find_element_by_xpath(self.costCenter_xpath).send_keys(Keys.ARROW_DOWN)
        self.driver.find_element_by_xpath(self.costCenter_xpath).send_keys(Keys.ENTER)
        self.driver.find_element_by_xpath(self.costCenter_xpath).send_keys(Keys.TAB)

    def click_Priority(self):
        time.sleep(2)
        self.driver.find_element_by_id(self.priority_id).click()
        # self.driver.find_element_by_xpath(self.priority_xpath).click()

    def click_Complexity(self):
        time.sleep(2)
        self.driver.find_element_by_id(self.complexity_id).click()
        # self.driver.find_element_by_id(self.complexity_id).click()
        # self.driver.find_element_by_xpath(self.complexity_xpath).click()

    def click_Confirm(self):
        self.driver.find_element_by_xpath(self.confirmButton_xpath).click()
        time.sleep(5)

    def click_OkButton(self):
        self.driver.find_element_by_xpath(self.okButton_xpath).click()
        # print("Custom Package Done")
    def customer_packagereq(self,PackageName,PackageDescription,Contract,SLA,CustomerRef,ContactPerson,PackageTechnology,OsDef,UploadFile,CostCenter):
        self.click_MakePackageReq()
        time.sleep(5)
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
        self.enter_ContactPerson(ContactPerson)
        time.sleep(3)
        self.enter_PackageTechnology(PackageTechnology)
        time.sleep(3)
        self.enter_OsDef(OsDef)
        time.sleep(3)
        self.enter_UploadFile(UploadFile)
        time.sleep(5)
        self.enter_CostCenter(CostCenter)
        self.click_Priority()
        time.sleep(3)
        self.click_Complexity()
        time.sleep(5)
        self.click_Confirm()
        time.sleep(5)
        self.click_OkButton()










