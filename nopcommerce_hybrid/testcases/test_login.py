import pytest
# from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readproperties  import ReadConfig
from utilities.customerLogger import LogGen

class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger=LogGen.loggen()

    @pytest.mark.regression
    def test_homePageTitle(self,setup):
        self.logger.info("*************** Test_001_Login *****************")
        self.logger.info("****Started Home page title test ****")
        self.driver = setup
        self.logger.info("****Opening URL****")
        self.driver.get(self.baseURL)
        act_title=self.driver.title

        if act_title=="Your store. Login":
            self.logger.info("**** Home page title test passed ****")
            self.driver.close()
            assert True
        else:
            self.logger.error("**** Home page title test failed****")
            self.driver.save_screenshot(".\\Screenshots\\"+"test_homePageTitle.png")
            self.driver.close()
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self,setup):

        self.logger.info("****Started Login Test****")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp=LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title=self.driver.title
        if act_title=="Dashboard / nopCommerce administration":
            self.logger.info("****Login test passed ****")
            self.driver.close()
            assert True
        else:
            self.logger.error("****Login test failed ****")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homePageTitle.png")
            self.driver.close()
            assert False

















'''
from pageObjects.LoginPage import LoginPage
from utilities.readproperties import Readconfig
from utilities.customerLogger import LogGen

class Test_001_Login:
    baseURL  = Readconfig.getApplicationURL()
    username = Readconfig.getUseremail()
    password = Readconfig.getPassword()

    logger= LogGen.loggen()

    def test_homePageTitle(self,setup):

        self.logger.info("********test_001_Login*************")
        self.logger.info("************Verifying Home Page Title****************")

        self.driver =setup
        self.driver.get(self.baseURL)
        act_title =self.driver.title
        self.driver.close()


        if act_title == "your store. Login":
            assert True
            self.driver.close()
            self.logger.info("***********Home page title test is passed **************")

        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homePageTitle.png")
            self.driver.close()
            self.logger.error("***********Home page title test is failed **************")
            assert False


    def test_login(self,setup):

        self.logger.info("*************")
        self.logger.info("************Verifying Login test****************")
        self.driver =setup
        self.driver.get(self.baseURL)
        self.lp= LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title =self.driver.title
        self.driver.close()

        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.logger.info("***********Login  test is passed **************")
            self.driver.close()
        else:

            self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
            self.driver.close()
            self.logger.error("***********Login  test is failed **************")
            assert False

'''