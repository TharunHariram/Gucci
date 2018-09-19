from selenium.webdriver.common.by import By
from base.basepage import BasePage
import time
import utilities.custom_logger as cl
import logging
from pages.home.login_page import LoginPage

class HomePage(LoginPage):


    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


        # locators:

    _header_id = "header-main"
    _footer_id = "footer-main"

    def verifyHeaderPresent(self):
        result = self.isElementPresent(self._header_id, locatorType="id")
        return result

    def verifyFooterPresent(self):
        result = self.isElementPresent(self._footer_id, locatorType='id')
        return result



