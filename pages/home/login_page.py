from selenium.webdriver.common.by import By
from base.basepage import BasePage
import time
import utilities.custom_logger as cl
import logging

class LoginPage(BasePage):


    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


     # locators:
    _signIn_link = "//li[@id='header-nav-signin']/a[1]"
    _user_name = 'j_username'
    _password_field = 'j_password'
    _stay_signedIn = "//form[@id='loginPageForm']/div[4]/div/label"
    _signIn_button = "//form[@id='loginPageForm']//button[contains(text(),'Sign In')]"
    _my_Account = "header-nav-signin-anchor"
    _signOut_Link = 'Sign Out'
    _search_Field = 'header-nav-search-input'

    # def getLoginLink(self):
    #     return self.driver.find_element(By.LINK_TEXT, self._login_link)
    #
    # def getEmailField(self):
    #     return self.driver.find_element(By.ID, self._email_field)
    #
    # def getPasswordField(self):
    #     return self.driver.find_element(By.ID, self._password_field)
    #
    # def getLoginButton(self):
    #     return self.driver.find_element(By.NAME, self._login_button)

    def clickSignInlink(self):
        self.actionChainsMethod(self._signIn_link, locatorType='xpath')

    def clickUsernameField(self):
        self.elementClick(self._user_name)

    def enterUsername(self,username):
        self.sendKeys(username, self._user_name, locatorType='id')


    def enterPassword(self,password):
        self.sendKeys(password, self._password_field, locatorType='id')

    def staySignedInCheckbox(self):
        self.elementClick(self._stay_signedIn, locatorType='xpath')

    def clickSignInButton(self):
        self.elementClick(self._signIn_button, locatorType='xpath')

    def verifyLoginSuccessful(self):
        result = self.isElementPresent("//div[@id='page']//span[contains(text(), 'Hariram')]", locatorType="xpath")
        return result

    def verifyLoginFailed(self):
        result = self.isElementPresent('//form[@id="loginPageForm"]//div[contains(text(),"Invalid email and/or password. Try again or click on")]', locatorType="xpath")
        return result

    def verifyLoginTitle(self):
        return self.verifyPageTitle("Gucci Official Site")


    def clickSearchField(self):
        self.elementClick(self._search_Field,locatorType='id')

    def clickMyAccount(self):
        self.actionChainsMethodHover(self._my_Account,locatorType='id')

    def clickSignOutLink(self):
        self.actionChainsMethod(self._signOut_Link,locatorType='link')


    def Login(self, username='', password=''):
        time.sleep(25)

        self.clickSignInlink()
        time.sleep(10)
        self.enterUsername(username)
        self.enterPassword(password)
        self.staySignedInCheckbox()
        self.clickSignInButton()
        time.sleep(20)
        #self.clickSearchField()
        #self.clickMyAccount()
        #self.clickSignOutLink()
