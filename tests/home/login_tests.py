from selenium import webdriver
from selenium.webdriver.common.by import By
import pages
import utilities
from https://github.com/TharunHariram/Gucci/tree/master/pages/pages.home.login_page import LoginPage
from utilities.teststatus import TestStatus
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import unittest
import pytest
import time

# comment to check in GIT 13

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class LoginTests(unittest.TestCase):


    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=2)
    def test_validlogin(self):
        # self.driver.get(self.baseurl)
        self.lp.Login("Tharun1567@gmail.com", "Ind@@143")
        result1 = self.lp.verifyLoginTitle()
        self.ts.mark(result1, "Title Verified")
        result2 = self.lp.verifyLoginSuccessful()
        self.ts.markFinal("test_validLogin", result2, "Login was successful")

    @pytest.mark.run(order=1)
    def test_invalidlogin(self):
        self.lp.Login("Tharun1567@gmail.com", "Ind@@14345")
        time.sleep(10)
        result = self.lp.verifyLoginFailed()
        assert result == True





