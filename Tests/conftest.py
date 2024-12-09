import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions


@pytest.fixture(scope="class", params=["chrome"])
def setup(request):
    """
    Pytest fixture to initialize the WebDriver based on the browser.
    Supports Chrome, Firefox, and Edge browsers.
    """
    global driver
    browser = request.param

    # Initialize WebDriver based on the browser parameter
    if browser == "chrome":
        chrome_options = ChromeOptions()
        chrome_service = ChromeService()
        driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
    elif browser == "firefox":
        firefox_options = FirefoxOptions()
        firefox_service = FirefoxService()
        driver = webdriver.Firefox(service=firefox_service, options=firefox_options)
    elif browser == "edge":
        edge_options = EdgeOptions()
        edge_service = EdgeService()
        driver = webdriver.Edge(service=edge_service, options=edge_options)
    else:
        raise ValueError(f"Unsupported browser: {browser}")

    # Open the target URL
    driver.maximize_window()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    time.sleep(4)  # Avoid unnecessary sleep; better to use WebDriver waits in actual tests

    # Assign driver to the test class
    request.cls.driver = driver

    # Yield driver for tests
    yield driver

    # Teardown WebDriver after tests
    driver.quit()
