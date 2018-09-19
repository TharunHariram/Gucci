from selenium import webdriver
from selenium.webdriver.common.by import By
import pages
import utilities
from pages.HomePage.Home_Page import HomePage
from utilities.teststatus import TestStatus
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import unittest
import pytest
import time
from base.selenium_driver import SeleniumDriver


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class HomePageTests(unittest.TestCase):


    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.hp = HomePage(self.driver)
        self.ts = TestStatus(self.driver)
        self.sd = SeleniumDriver(self.driver)

    @pytest.mark.run(order=1)
    def test_validload(self):
        result1 = self.hp.verifyHeaderPresent()
        assert result1
        self.sd.screenShot(resultMessage='Header Present')
        time.sleep(10)
        self.hp.actionChainsMethodScrollBottomPage()
        result2 = self.hp.verifyFooterPresent()
        assert result2
        self.sd.screenShot(resultMessage='Footer Present')
        self.ts.markFinal("test_validLoad", result1, "Header Successfully present")
        self.ts.markFinal("test_validLoad", result2, "Footer Successfully present")
