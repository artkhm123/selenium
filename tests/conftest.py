import os
import pytest
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FFService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium import webdriver



def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--drivers", action="store", default=os.path.expanduser("~\\khomiakov_a\\Desktop\\Python\\drivers\\"))
    parser.addoption("--url", action="store", default="http://192.168.31.28:8081")
@pytest.fixture
def browser(request):
    _browser = request.config.getoption("--browser")
    _drivers_path = request.config.getoption("--drivers")
    _url = request.config.getoption("--url")
    # headless = request.config.getoption("--headless")
    driver = None
    if _browser == "chrome":
        service = ChromeService(executable_path=_drivers_path + "chromedriver")
        driver = webdriver.Chrome(service=service)
        # options = ChromeOptions()
        # options.headless = headless
    elif _browser == "ff" or _browser == "firefox":
        service = FFService(executable_path=_drivers_path + "geckodriver")
        driver = webdriver.Firefox(service=service)
        # options = FirefoxOptions()
        # # options.headless = headless
    elif _browser == "yandex" or _browser == "ya":
        service = ChromeService(executable_path=_drivers_path + "yandexdriver")
        driver = webdriver.Chrome(service=service)
        # options = ChromeOptions()
        # options.headless = headless
    elif _browser == "edge":
        service = EdgeService(executable_path=_drivers_path + "msedgedriver")
        driver = webdriver.Edge(service=service)
        # options = ChromeOptions()
        # options.headless = headless
    driver.get(_url)
    driver.url= _url
    driver.maximize_window()
    yield driver
    driver.quit()