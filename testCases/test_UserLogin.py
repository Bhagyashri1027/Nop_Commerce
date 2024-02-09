import allure
import pytest

from pageObjects.LoginPage import LoginClass
from utilities.readconfingfile import Readconfig
from utilities.Logger import LoggenClass


class Test_Login:
    email = Readconfig.get_email()
    password = Readconfig.get_password()
    log = LoggenClass.log_generator()


    @allure.feature("Page Title")
    @allure.story("Verifying th page title")
    @allure.issue("ABC-123")
    @allure.link("https://admin-demo.nopcommerce.com/",name='nop commerce website')
    @allure.title('NopCom- Test page title')
    @allure.description('My test description')
    @allure.link("https://admin-demo.nopcommerce.com/")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.m1
    def test_verify_url_001(self, setup):
        self.log.info("test case:test_verify_url_001 is started")
        self.driver = setup
        self.log.info("Opening browser and navigating to demo nop_commerce")
        self.log.info("Page title is ->,"+self.driver.title)
        if self.driver.title == "Your store. Login":
            self.log.info("test case test_verify_url_001 is passed")
            self.log.info("Taking screenshots")
            self.driver.save_screenshot("..\\Screenshots\\test_verify_url_001_Pass.png")
            assert True
        else:
            self.log.info("test case test_verify_url_001 is failed")
            self.log.info("Taking screenshots")
            self.driver.save_screenshot("..\\Screenshots\\test_verify_url_001_Fail.png")
            assert False
        self.log.info("test case test_verify_url_001 completed")

    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.m1
    def test_user_login_002(self, setup):
        self.log.info("test case test_user_login_002 is stared")
        self.driver = setup
        self.log.info("Opening browser and navigating to demo nop_commerce")
        self.lp = LoginClass(self.driver)
        self.log.info("Entering email -"+self.email)
        self.lp.enter_email(self.email)
        self.log.info("Entering password -" + self.password)
        self.lp.enter_password(self.password)
        self.log.info("click on login button")
        self.lp.click_login()
        if self.lp.varify_login_status() == "Login Pass":
            self.log.info("test case test_user_login_002 is passed")
            self.log.info("Taking screenshot")
            self.driver.save_screenshot("..\\Screenshots\\test_user_login_002_Pass.png")
            self.log.info("click on logout button ")
            self.lp.click_logout()
            assert True
        else:
            self.log.info("test case test_user_login_002 is failed")
            self.log.info("Taking screenshot")
            self.driver.save_screenshot("..\\Screenshots\\test_user_login_002_Fail.png")
            assert False
        self.log.info("test case test_user_login_002 is completed")


# pytest -v -n=2 -m sanity --alluredir="D:\Python Automation Practicals\Pytest Practicals\nopCommerce_Testing\AllureReports --browser firefox -p no:warnings"