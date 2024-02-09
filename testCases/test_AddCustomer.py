import random
import string
import time

import allure
import pytest
from pageObjects.AddCustomerPage import AddCustomerClass
from pageObjects.LoginPage import LoginClass
from utilities.readconfingfile import Readconfig
from utilities.Logger import LoggenClass


class Test_Add_Customer:
    email = Readconfig.get_email()
    password = Readconfig.get_password()
    log = LoggenClass.log_generator()

    @allure.story("Customer")
    @pytest.mark.m2
    def test_addCustomer_003(self, setup):
        self.log.info("test case test_addCustomer_003 is stared")
        self.driver = setup
        self.log.info("Opening browser and navigating to demo nop_commerce")
        self.lp = LoginClass(self.driver)
        self.log.info("Entering email -" + self.email)
        self.lp.enter_email(self.email)
        self.log.info("Entering password -" + self.password)
        self.lp.enter_password(self.password)
        self.log.info("click on login button")
        self.lp.click_login()
        self.ac = AddCustomerClass(self.driver)
        self.log.info("Click on customer menu")
        self.ac.Click_Customers_Menu()
        self.log.info("Click on customer  submenu")
        self.ac.Click_Customers_SubMenu()
        self.log.info("Click on add customer")
        self.ac.Click_AddNewCustomer()
        email = Generate_Email()
        self.log.info("EMail-->" + email)
        self.log.info("Enter email")
        self.ac.Enter_Email(email)  # Generate_email()function to passing to function
        self.log.info("Enter password")
        self.ac.Enter_Password("Crednce@101")
        self.log.info("Enter FirstName")
        self.ac.Enter_FirstName("Pallavi")
        self.log.info("Enter LastName")
        self.ac.Enter_LastName("chavan")
        self.log.info("Enter LastName")
        self.log.info("Select Gender")
        self.ac.Select_Gender("Female")
        self.log.info("Enter Date of birth")
        self.ac.Enter_DOB("12/2/1994")
        self.log.info("Enter Company Name")
        self.ac.Enter_CompanyName("Credence")
        self.log.info("Click on  Is tax exempt CheckBox")
        self.ac.CheckBox_Tax()
        self.log.info("Click on Newsletter")
        self.ac.Click_Newsletter()
        self.log.info("Click on Newsletter List")
        self.ac.Click_Newsletter_List()
        self.log.info("Select value for manager of vendor")
        self.ac.DropDown_Manager_Of_Vendor("1")
        self.log.info("Click on Active checkbox")
        self.ac.Click_CheckBox_Active()
        self.log.info("Enter comment")
        self.ac.Enter_comment("Credence is best")
        self.log.info("Click on save Button")
        self.ac.Click_SaveButton()
        if self.ac.Validate_Success_Message() == "pass":
            self.log.info("Test_case test_addCustomer_003 is passed")
            self.driver.save_screenshot("..\\Screenshots\\test_AddCustomer_003_Pass.png")
            assert True
        else:
            self.log.info("Test_case test_addCustomer_003 is Failed")
            self.driver.save_screenshot("..\\Screenshots\\test_AddCustomer_003_Fail.png")
            assert False
        self.log.info("test case test_AddCustomer_003 is completed")

def Generate_Email():
    username = ''.join(random.choices(string.ascii_lowercase,k=5))
    domain = random.choice(['gmail.com', 'ymail.com', 'outlook.com'])
    return f"{username}@{domain}"
