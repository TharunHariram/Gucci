import pytest
from selenium import webdriver
from base.webdriverfactory import WebDriverFactory
from pages.home.login_page import LoginPage

@pytest.fixture()
def setUp():
    print("I amd gonna run before every method")
    yield
    print("I am gonna run after every method")

@pytest.fixture(scope='class')
def oneTimeSetUp(request, browser):
    print("I amd gonna once before every module")
    wdf = WebDriverFactory(browser)
    driver = wdf.getWebDriverInstance()
    # lp = LoginPage(driver)
    # lp.Login("Tharun1567@gmail.com", "Ind@@143")
    # if browser == 'Firefox':
    #     baseurl = 'https://www.gucci.com/us/en/'
    #     driver = webdriver.Firefox()
    #     driver.maximize_window()
    #     driver.implicitly_wait(50)
    #     driver.get(baseurl)
    #     print('Running tests on Firefox')
    # else:
    #     baseurl = 'https://www.gucci.com/us/en/'
    #     driver = webdriver.Chrome()
    #     driver.get(baseurl)
    #     print('Running tests on Chrome')

    if request.cls is not None:
        request.cls.driver = driver

    yield driver
    driver.quit()
    print("Running one Time teardown")

def pytest_addoption(parser):
    parser.addoption('--browser')
    parser.addoption('--ostype', help="type of Operating system")

@pytest.fixture(scope='session')
def browser(request):
    return request.config.getoption('--browser')

@pytest.fixture(scope='session')
def ostype(request):
    return request.config.getoption('--ostype')