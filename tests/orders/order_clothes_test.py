from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.orders.order_clothes_page import OrderClothesPage
from utilities.teststatus import TestStatus
import unittest
import pytest
import time



@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
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
    def test_orderClothes(self):
        self.ocp.SearchOrder("Gucci Cities cotton T-shirt","5326761129661929","811","Tharun Hariram")
        print("shopping successful")
        result1 = self.ocp.verifyOrderCreationSuccessful()
        self.ts.markFinal("test_validOrderCreation", result1, "Order successfully created")


