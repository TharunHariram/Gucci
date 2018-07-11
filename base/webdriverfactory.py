"""
@package base

WebDriver Factory class implementation
It creates a webdriver instance based on browser configurations

Example:
    wdf = WebDriverFactory(browser)
    wdf.getWebDriverInstance()
"""
import traceback
from selenium import webdriver
import os

class WebDriverFactory():

    def __init__(self, browser):
        """
        Inits WebDriverFactory class

        Returns:
            None
        """
        self.browser = browser
    """
        Set chrome driver and iexplorer environment based on OS

        chromedriver = "C:/.../chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = chromedriver
        self.driver = webdriver.Chrome(chromedriver)

        PREFERRED: Set the path on the machine where browser will be executed
    """

    def getWebDriverInstance(self):
        """
       Get WebDriver Instance based on the browser configuration

        Returns:
            'WebDriver Instance'
        """
        baseURL = "https://www.gucci.com/us/en/"
        if self.browser == "iexplorer":
            # Set ie driver
            iedriver = "C:\\Users\\harirath\\Documents\\Vodafone Germany\\Selenium_Drivers\\libs\\IEDriverServer.exe"
            os.environ["webdriver.ie.driver"] = iedriver
            driver = webdriver.Ie(iedriver)
        elif self.browser == "firefox":
            driver = webdriver.Firefox()
        elif self.browser == "chrome":
            # Set chrome driver
            chromedriver = "C:\\Users\\harirath\\Documents\\Vodafone Germany\\Selenium_Drivers\\libs\\chromedriver.exe"
            os.environ["webdriver.ie.driver"] = chromedriver
            driver = webdriver.Chrome(chromedriver)
        else:
            driver = webdriver.Firefox()
        # Setting Driver Implicit Time out for An Element
        driver.implicitly_wait(50)
        # Maximize the window
        driver.maximize_window()
        # Loading browser with App URL
        driver.get(baseURL)
        return driver