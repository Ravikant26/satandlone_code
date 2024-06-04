import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from pageObjects.Login_Page import Login_Class
from utilities.Logger import Logging_Class
from utilities.readConfigFile import ReadconfigClass


# driver--> confest
# testcases--> driver--> methods which are defined in page-objects login class
# screenshots
# logs
# reports --> 1.html 2.allure report
# config -- > hardcode value replace

class Test_CredKart_Login:

    log = Logging_Class.log_generator()
    Email = ReadconfigClass.getEmail()
    Password = ReadconfigClass.getPassword()

    def test_CredKart_url_001(self, setup):
        # self.log.debug(" this is debug")
        # self.log.info(" this is info")
        # self.log.warning(" this is warning")
        # self.log.error(" this is error")
        # self.log.critical(" this is critical")
        self.log.info("Testcase test_CredKart_url_001 is started")
        self.log.info("Opening browser")
        self.driver = setup
        self.log.info("Check Page Title")
        if self.driver.title == "CredKart":
            self.log.info("Taking Screenshot")

            self.driver.save_screenshot(".\\Screenshots\\test_CredKart_url_001_pass.PNG")
            self.log.info("Testcase test_CredKart_url_001 is Pass")
            assert True
        else:
            self.log.info("Taking Screenshot")
            self.driver.save_screenshot(".\\Screenshots\\test_CredKart_url_001_fail.PNG")
            self.log.info("Testcase test_CredKart_url_001 is Fail")
            assert False
        self.log.info("Testcase test_CredKart_url_001 is Completed\n")



    def test_user_login_002(self, setup):
        self.log.info("Testcase test_user_login_002 is started")
        self.log.info("Opening browser")
        self.driver = setup
        self.lg = Login_Class(self.driver)
        self.log.info("Click On login Link")
        self.lg.Login_Link()
        self.log.info("Enter Email" + self.Email)
        self.lg.Enter_Email(self.Email)
        self.log.info("Enter Password" + self.Password)
        self.lg.Enter_Password(self.Password)
        self.log.info("Click Login Button")
        self.lg.Click_Login_Button()
        self.log.info("Verify Login Stauts")
        if self.lg.Verify_Login_Status() == "Pass":
            self.log.info("Taking screenshot")
            self.driver.save_screenshot(".\\Screenshots\\test_user_login_002_pass.PNG")
            self.log.info("Testcase test_user_login_002 is Pass")
            assert True
        else:
            self.log.info("Testcase test_user_login_002 is Fail")
            self.log.info("Taking screenshot")
            self.driver.save_screenshot(".\\Screenshots\\test_user_login_002_fail.PNG")
            assert False
        self.log.info("Testcase test_user_login_002 is Completed\n")

# pytest -v --html=HtmlReports/my_report_firefox.html -n=4