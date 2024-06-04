
from pageObjects.Login_Page import Login_Class
from utilities.Logger import Logging_Class
from utilities import XLUTILIES


class Test_CredKart_Login_DDT:

    log = Logging_Class.log_generator()
    path = ".\\Test_Data\\UserLogin.xlsx"

    def test_CredKart_url_DDT_002(self, setup):
        self.log.info("Testcase test_CredKart_url_DDT_002 is started")
        self.log.info("Opening browser")
        self.driver = setup
        self.lg = Login_Class(self.driver)
        self.log.info("Click On login Link")
        self.lg.Login_Link()
        self.rows = XLUTILIES.rows_count(self.path,'Sheet1')
        print("Number of rows in Login data excel --> " + str(self.rows))
        Result_List = []
# 5
        for r in range(2, self.rows+1):
            print("Loop Number --> " + str(r))
            self.Email = XLUTILIES.read_data(self.path,'Sheet1', r,1)
            self.Password = XLUTILIES.read_data(self.path, 'Sheet1', r, 2)
            self.exp_result = XLUTILIES.read_data(self.path, 'Sheet1', r, 3)

            self.log.info("Enter Email" + self.Email)
            self.lg.Enter_Email(self.Email)
            self.log.info("Enter Password" + self.Password)
            self.lg.Enter_Password(self.Password)
            self.log.info("Click Login Button")
            self.lg.Click_Login_Button()
            self.log.info("Verify Login Stauts")
            if  self.exp_result == "Login_Pass" and self.lg.Verify_Login_Status() == "Pass" :
                self.log.info("Taking screenshot")
                self.driver.save_screenshot(".\\Screenshots\\test_user_login_002_pass.PNG")
                XLUTILIES.read_write(self.path, 'Sheet1', r, 4, "Login_Pass")
                Result_List.append("Pass")
                self.lg.Click_Menu_Button()
                self.lg.Click_Logout_Button()
                self.lg.Login_Link()
            elif self.exp_result == "Login_Pass" and self.lg.Verify_Login_Status() == "Fail" :
                self.log.info("Taking screenshot")
                self.driver.save_screenshot(".\\Screenshots\\test_user_login_002_fail.PNG")
                XLUTILIES.read_write(self.path, 'Sheet1', r, 4, "Login_Fail")
                Result_List.append("Fail")
                self.lg.Login_Link()
            elif self.exp_result == "Login_Fail" and self.lg.Verify_Login_Status() == "Pass" :
                self.log.info("Taking screenshot")
                self.driver.save_screenshot(".\\Screenshots\\test_user_login_002_fail.PNG")
                XLUTILIES.read_write(self.path, 'Sheet1', r, 4, "Login_Fail")
                Result_List.append("Fail")
                self.lg.Click_Menu_Button()
                self.lg.Click_Logout_Button()
                self.lg.Login_Link()
            elif self.exp_result == "Login_Fail" and self.lg.Verify_Login_Status() == "Fail":
                self.log.info("Taking screenshot")
                self.driver.save_screenshot(".\\Screenshots\\test_user_login_002_pass.PNG")
                XLUTILIES.read_write(self.path, 'Sheet1', r, 4, "Login_Fail")
                Result_List.append("Pass")
                self.lg.Login_Link()

        print(Result_List)
        if "Fail" in Result_List:
            self.log.info("Testcase test_user_login_DDT_002 is Fail")
            assert False
        else:
            self.log.info("Testcase test_user_login_DDT_002 is Pass")
            assert True
        self.log.info("Testcase test_user_login_DDT_002 is Completed\n")


