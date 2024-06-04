import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

#to customise the command line
# added --browser parameter to command line
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")


# we need to add command liner --browser
def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture
def setup(request):
    browser = request.config.getoption("--browser")
    if browser == "chrome":
        print("Test Run - Browser Chrome")
        driver = webdriver.Chrome()
    elif browser == "firefox":
        print("Test Run - Browser Firefox")
        driver = webdriver.Firefox()
    elif browser == "edge":
        print("Test Run - Browser Edge")
        driver = webdriver.Edge()
    else:
        #driver = webdriver.Chrome()
        print("Test Run - Browser Headless")
        driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    driver.get("https://automation.credence.in/shop")
    driver.implicitly_wait(5)
    yield driver
    driver.quit()

    #
    # yield
    # driver.quit()