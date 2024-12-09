from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Kpi:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def configure(self):
        locators = [
            (By.LINK_TEXT, "Performance"),
            (By.XPATH, "//span[normalize-space()='Configure']//i[@class='oxd-icon bi-chevron-down']"),
            (By.XPATH, "//a[@class='oxd-topbar-body-nav-tab-link'][1]"),
            (By.XPATH, "//button[normalize-space()='Add']"),
            (By.XPATH, "//button[normalize-space()='Cancel']")
        ]

        elements = []
        for i in locators:
            element = self.driver.find_element(i)
            elements.append(element)
            self.wait_and_click(element)

    def add(self):
        locators = {
            "add_button": (By.XPATH, "//button[normalize-space()='Add']"),
            "kpi_input": (By.XPATH, "(//input[@class='oxd-input oxd-input--active'])[2]"),
            "job_select": (By.CSS_SELECTOR, ".oxd-select-text-input"),
            "job_title": (By.XPATH, "(//span[normalize-space()='Chief Executive Officer'])[1]"),
            "min_rating": (By.XPATH, "(//input[@modelmodifiers='[object Object]'])[1]"),
            "save_button": (By.CSS_SELECTOR, "button[type='submit']"),
            "cancel_button": (By.XPATH, "//button[normalize-space()='Cancel']")
        }

        self.wait_and_click(locators["add_button"])
        self.wait_and_send_keys(locators["kpi_input"], "New KPI")
        self.wait_and_click(locators["job_select"])
        self.wait_and_click(locators["job_title"])
        self.wait_and_send_keys(locators["min_rating"], "40")
        self.wait_and_click(locators["save_button"])
        self.wait_and_click(locators["cancel_button"])

    def wait_and_click(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def wait_and_send_keys(self, locator, text):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.send_keys(text)




