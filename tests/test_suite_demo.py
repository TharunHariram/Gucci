import unittest
from tests.home.login_tests import LoginTests
from tests.orders.order_clothes_test import OrderClothesTests

# Get all tests from test classes

tc1 = unittest.TestLoader().loadTestsFromTestCase(LoginTests)
tc2 = unittest.TestLoader().loadTestsFromTestCase(OrderClothesTests)

# create a test suite combining all test classes
smokeTest = unittest.TestSuite([tc1])
unittest.TextTestRunner(verbosity=2).run(smokeTest)