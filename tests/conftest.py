import pytest
from selenium import webdriver
driver = None


# random browser selection method
def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome")


@pytest.fixture(scope='class')
def setup(request):
    global driver
    # random browser selection through cmd
    browser_name = request.config.getoption('browser_name')
    if browser_name == "chrome":
        driver = webdriver.Chrome()
    elif browser_name == "firefox":
        driver = webdriver.Firefox()
    elif browser_name == "Edge":
        driver = webdriver.Edge()
        driver.implicitly_wait(4)
    driver.get("https://openweathermap.org/")
    driver.maximize_window()
    driver.implicitly_wait(20)
    # driver initialisation to class level
    request.cls.driver = driver
    yield
    driver.close()
