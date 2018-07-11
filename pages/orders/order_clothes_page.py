from selenium.webdriver.common.by import By
from base.basepage import BasePage
import time
import utilities.custom_logger as cl
import logging

class OrderClothesPage(BasePage):

    log =cl.customLogger(logging.DEBUG)

    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    # locators
    _popup = "//div[@id='international-overlay']//button[@type='button']"
    _signIn_link = "//li[@id='header-nav-signin']/a[1]"
    _user_name = 'j_username'
    _password_field = 'j_password'
    _stay_signedIn = "//form[@id='loginPageForm']/div[4]/div/label"
    _signIn_button = "//form[@id='loginPageForm']//button[contains(text(),'Sign In')]"

    _search_field = "//form[@id='header-nav-search']/input[@type = 'submit']"
    _search_Field_Enter = "header-nav-search-input"
    _search_Field_Submit = "//form[@id='header-nav-search']/input[@type = 'submit']"
    _result_Selection = "//div[@class='product-tiles-grid-item-image']//img[@alt='Gucci Cities cotton T-shirt']"
    _select_Size_Dropdown = "//form[@id='product-detail-add-to-shopping-bag-form']//div[@class='selectric']//b[@class='button']"
    _select_Size_Value = "//form[@id='product-detail-add-to-shopping-bag-form']//div[@class='selectricScroll']//ul//li//span[text()='large']"
    _add_To_Shopping_Bag = "//form[@id='product-detail-add-to-shopping-bag-form']/button"
    # _bag = "//a[@id='header-nav-bag-anchor']//span[text()='Bag']"
    _bag = "header-nav-bag-wrapper"
    _checkout = "//div[@id='page']//a[@class='button-standard']"
    _credit_Card_List_DD = "//form[@id='credit-card-order']//div[@class='selectric']//p[@class='label gold']"
    _credit_Card_Type = "//form[@id='credit-card-order']//div[@class='selectricScroll']//ul//li//span[text()='MasterCard']"
    _credit_Card_Number = "input-credit-card-number"
    _credit_card_Security_Code = "input-credit-card-code-new"
    _name_On_Card = "input-credit-card-name"
    _expiration_Date_MM_List = "//form[@id='credit-card-order']//div[@class='selectric']//p[text()='MM']"
    _expiration_Date_MM = "//form[@id='credit-card-order']//div[@class='selectricScroll']//ul//li[text()='02']"
    _expiration_Date_YYYY_List = "//form[@id='credit-card-order']//div[@class='selectric']//p[text()='YYYY']"
    _expiration_Date_YYYY = "//form[@id='credit-card-order']//div[@class='selectricScroll']//ul//li[text()='2023']"
    _confirm_Details = "//form[@id = 'credit-card-order']//button[text()='Confirm Details']"


    def clickPopUp(self):
        self.elementClick(self._popup,locatorType='xpath')

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

    def verifyOrderCreationSuccessful(self):
        result = self.isElementPresent("//div[@id='tooltip-credit-card-number']/div[contains(text(),'Please enter a valid card number')]", locatorType="xpath")
        return result



    def Login(self, username='', password=''):
        time.sleep(5)
        self.clickPopUp()
        time.sleep(5)
        self.clickSignInlink()
        time.sleep(10)
        self.enterUsername(username)
        self.enterPassword(password)
        self.staySignedInCheckbox()
        self.clickSignInButton()
        time.sleep(20)

    def clickSearchField(self):
        self.elementClick(self._search_field, locatorType='xpath')

    def enterSearchElement(self,searchElement):
        self.sendKeys(searchElement,self._search_Field_Enter,locatorType='id')

    def clickSearchFieldSubmit(self):
        self.elementClick(self._search_Field_Submit,locatorType='xpath')

    def selectResult(self):
        self.actionChainsMethod(self._result_Selection,locatorType='xpath')

    def selectSizeDropdown(self):
        self.elementClick(self._select_Size_Dropdown,locatorType='xpath')

    def selectSizeValue(self):
        self.elementClick(self._select_Size_Value,locatorType='xpath')

    def clickAddToShoppingBag(self):
        self.elementClick(self._add_To_Shopping_Bag,locatorType='xpath')

    def clickBag(self):
        self.actionChainsMethod(self._bag,locatorType='id')

    def clickCheckout(self):
        self.actionChainsMethodScrollBy100(self._checkout,locatorType='xpath')

    def clickCreditCardListDD(self):
        self.elementClick(self._credit_Card_List_DD,locatorType='xpath')

    def selectCreditCardType(self):
        self.elementClick(self._credit_Card_Type,locatorType='xpath')

    def enterCreditCardNumber(self,creditcardnumber):
        self.sendKeys(creditcardnumber,self._credit_Card_Number,locatorType='id')

    def enterCreditCardSecurityCode(self,creditcardsecuritycode):
        self.sendKeys(creditcardsecuritycode,self._credit_card_Security_Code, locatorType='id')

    def enterNameOnCard(self, nameoncard):
        self.sendKeys(nameoncard,self._name_On_Card, locatorType='id')

    def clickExpirationDateMMList(self):
        self.elementClick(self._expiration_Date_MM_List, locatorType='xpath')

    def selectExpirationDateMM(self):
        self.elementClick(self._expiration_Date_MM,locatorType='xpath')

    def clickExpirationDateYYYYList(self):
        self.elementClick(self._expiration_Date_YYYY_List,locatorType='xpath')

    def selectExpirationDateYYYY(self):
        self.elementClick(self._expiration_Date_YYYY, locatorType='xpath')

    def clickConfirmDetails(self):
        self.actionChainsMethodScrollBy200(self._confirm_Details,locatorType='xpath')

    def clickCreditCardNumber(self):
        self.elementClick(self._credit_Card_Number,locatorType='id')



    def SearchOrder(self,searchElement,creditcardnumber,creditcardsecuritycode,nameoncard):
        self.clickSearchField()
        self.enterSearchElement(searchElement)
        self.clickSearchFieldSubmit()
        time.sleep(5)
        self.selectResult()
        time.sleep(20)
        self.selectSizeDropdown()
        time.sleep(3)
        self.selectSizeValue()
        self.clickAddToShoppingBag()
        time.sleep(15)
        self.clickBag()
        time.sleep(5)
        self.clickCheckout()
        time.sleep(10)
        self.clickCreditCardListDD()
        time.sleep(2)
        self.selectCreditCardType()
        self.enterCreditCardNumber(creditcardnumber)
        self.enterCreditCardSecurityCode(creditcardsecuritycode)
        self.enterNameOnCard(nameoncard)
        self.clickExpirationDateMMList()
        time.sleep(2)
        self.selectExpirationDateMM()
        self.clickExpirationDateYYYYList()
        time.sleep(2)
        self.selectExpirationDateYYYY()
        self.clickConfirmDetails()
        time.sleep(6)
        self.clickCreditCardNumber()






