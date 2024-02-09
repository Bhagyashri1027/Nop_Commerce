import pytest
from selenium import webdriver

'''Multiple browser invocation for this we need of command liner (--browser) argument and we can pass browser 
name at the time execution.Also we can make run.bat file which have command for different browser 
so, when we click on run.bat same testcase in execute in different '''


def pytest_addoption(parser):
    parser.addoption("--browser")


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")


@pytest.fixture
def setup(request):
    browser = request.config.getoption("--browser")
    if browser == "chrome":
        print("Test Run- Browser Chrome")
        driver = webdriver.Chrome()
    elif browser == "firefox":
        print("Test Run- Browser Firefox")
        driver = webdriver.Firefox()
    elif browser == "edge":
        print("Test Run- Browser Edge")
        driver = webdriver.Edge()
    else:
        print("Test Run- Browser Headless")
        driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    driver.get("https://admin-demo.nopcommerce.com/")
    driver.implicitly_wait(5)
    yield driver
    driver.quit()


# pytest -v -n=2 -m m1 --alluredir="D:\Python Automation Practicals\Pytest Practicals\nopCommerce_Testing\
# AllureReports" --browser chrome -p no:warning

