from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.orders.order_clothes_page import OrderClothesPage
from utilities.teststatus import TestStatus
import unittest
import pytest
import time
from ddt import ddt, data, unpack


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
@ddt
class OrderClothesTests(unittest.TestCase):


    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.ocp = OrderClothesPage(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=1)
    def test_login(self):
        # self.driver.get(self.baseurl)
        self.ocp.Login("Tharun1567@gmail.com", "Ind@@143")
        result1 = self.ocp.verifyLoginSuccessful()
        self.ts.markFinal("test_validLogin", result1, "Login was successful")

    @pytest.mark.run(order=2)
    @data(("Gucci Cities cotton T-shirt","5326761129661929","811","Tharun Hariram"), ("Other product","5326761129661938","812","Tharun Test"))
    @unpack
    def test_orderClothes(self,clothName, ccNum, ccCvv, ccName):
        self.ocp.SearchOrder(searchElement=clothName,creditcardnumber=ccNum,creditcardsecuritycode=ccCvv,nameoncard=ccName)
        print("shopping successful")
        result1 = self.ocp.verifyOrderCreationSuccessful()
        self.ts.markFinal("test_validOrderCreation", result1, "Order successfully created")


