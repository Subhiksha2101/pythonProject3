from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import StaleElementReferenceException
from urllib3.util import timeout
from selenium.webdriver.chrome.service import Service


def test_perfor():
    driver = webdriver.Chrome()
    driver.get('https://opensource-demo.orangehrmlive.com/')
    driver.maximize_window()

    time.sleep(5)
    usernam = driver.find_element(By.NAME, "username").send_keys("Admin")
    passw = driver.find_element(By.CSS_SELECTOR, ".oxd-input.oxd-input--active").send_keys("admin123")
    submit = driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    time.sleep(10)

    # performance
    driver.find_element(By.LINK_TEXT, "Performance").click()
    time.sleep(5)

    # a= driver.find_element(By.XPATH,"//span[normalize space()='Quality Assurance']")
    # driver.execute_script("arguments[0].scrollIntoView(true);",a)
    # time.sleep(5)

    # Configure
    driver.find_element(By.XPATH, "//span[normalize-space()='Configure']//i[@class='oxd-icon bi-chevron-down']").click()
    time.sleep(5)

    # kpi
    driver.find_element(By.XPATH, "//a[@class='oxd-topbar-body-nav-tab-link'][1]").click()
    time.sleep(5)

    # select
    # driver.find_element(By.XPATH,"//*[contains(text(),'oxd-select-text oxd-select-text--focus')][1]").click()
    driver.find_element(By.CSS_SELECTOR, ".oxd-select-text-input").click()
    time.sleep(5)

    # scroll
    a = driver.find_element(By.XPATH, "//span[text()='HR Manager']")
    driver.execute_script("arguments[0].scrollIntoView(true);", a)
    time.sleep(5)
    a.click()
    time.sleep(5)
    # scroll up
    # b=driver.find_element(By.XPATH,"//span[normalize-space()='(50) Records Found']")
    driver.execute_script("window.scrollTo(0,0);")
    # b.click()
    time.sleep(5)
    # search
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(5)

    # scroll down
    a = driver.find_element(By.CSS_SELECTOR, "[type='button']")
    driver.execute_script("arguments[0].scrollIntoView(true);", a)
    time.sleep(5)

    # checkbox
    checkbox = driver.find_element(By.XPATH, "(//i[@class='oxd-icon bi-check oxd-checkbox-input-icon'])[4]").click()
    time.sleep(5)
    # delete
    driver.find_element(By.XPATH, "(//button[normalize-space()='Delete Selected'])[1]").click()
    time.sleep(5)
    driver.find_element(By.CSS_SELECTOR,
                        "button[class='oxd-button oxd-button--medium oxd-button--label-danger orangehrm-button-margin']").click()
    time.sleep(5)
    # checkbox
    checkboxs = driver.find_element(By.XPATH, "(//i[@class='oxd-icon bi-check oxd-checkbox-input-icon'])[4]").click()
    time.sleep(5)
    # delete
    driver.find_element(By.XPATH, "(//button[normalize-space()='Delete Selected'])[1]").click()
    time.sleep(5)
    driver.find_element(By.XPATH, "//button[normalize-space()='No, Cancel']").click()
    time.sleep(5)
    # reset
    driver.find_element(By.CSS_SELECTOR, "button[type='reset']").click()
    time.sleep(5)
    # trash
    driver.find_element(By.XPATH, "(//i[@class='oxd-icon bi-trash'])[1]").click()
    time.sleep(5)
    # yes delete
    driver.find_element(By.CSS_SELECTOR,
                        "button[class='oxd-button oxd-button--medium oxd-button--label-danger orangehrm-button-margin']").click()
    time.sleep(5)
    # trash
    driver.find_element(By.XPATH, "(//i[@class='oxd-icon bi-trash'])[1]").click()
    time.sleep(5)
    # no delete
    driver.find_element(By.XPATH, "//button[normalize-space()='No, Cancel']").click()
    time.sleep(5)
    # pencil
    driver.find_element(By.XPATH, "(//i[@class='oxd-icon bi-pencil-fill'])[1]").click()
    time.sleep(5)
    # edit KPI
    driver.find_element(By.XPATH, "(//input[@class='oxd-input oxd-input--active'])[2]").send_keys("Service")
    # job title
    driver.find_element(By.XPATH, "//div[@class='oxd-select-text-input']").click()
    time.sleep(5)
    driver.find_element(By.XPATH, "//span[normalize-space()='Chief Executive Officer']").click()
    time.sleep(5)
    # Min rating
    # driver.find_element(By.XPATH, "(//input[@modelmodifiers='[object Object]'])[1]").send_keys("80")
    # time.sleep(5)
    # # Max rating
    # max = driver.find_element(By.XPATH, "(//input[@modelmodifiers='[object Object]'])[2]")
    # actions = ActionChains(driver)
    # actions.key_down(Keys.CONTROL).send_keys("a").key_down(Keys.CONTROL).send_keys(Keys.DELETE).perform()
    # time.sleep(5)
    # max.send_keys("88")

    # switch
    driver.find_element(By.XPATH,
                        "(//span[@class='oxd-switch-input oxd-switch-input--active --label-right'])[1]").click()
    time.sleep(5)
    # save
    driver.find_element(By.XPATH, "//button[normalize-space()='Cancel']").click()
    time.sleep(5)
    # driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    # time.sleep(5)
    # Add
    a = driver.find_element(By.XPATH, "//button[normalize-space()='Add']")
    time.sleep(5)
    driver.execute_script("arguments[0].scrollIntoView(true);", a)
    time.sleep(5)
    # pencil
    driver.find_element(By.XPATH, "(//i[@class='oxd-icon bi-pencil-fill'])[1]").click()
    time.sleep(5)
    # cancel
    driver.find_element(By.XPATH, "//button[normalize-space()='Cancel']").click()
    time.sleep(5)

    # Add
    # driver.find_element(By.XPATH, "//button[normalize-space()='Add']").click()
    # time.sleep(5)
    # # key performanze Indicator
    # driver.find_element(By.XPATH, "(//input[@class='oxd-input oxd-input--active'])[2]").send_keys("Service")
    # time.sleep(5)
    # # job title
    # driver.find_element(By.CSS_SELECTOR, ".oxd-select-text-input").click()
    # time.sleep(5)
    # driver.find_element(By.XPATH, "(//span[normalize-space()='Chief Executive Officer'])[1]").click()
    # time.sleep(5)
    # # Minimum rating
    # driver.find_element(By.XPATH, "(//input[@class='oxd-input oxd-input--focus oxd-input--error'])[1]").send_keys("80")
    # time.sleep(5)
    # # driver.find_element(By.XPATH,"(//input[@class='oxd-input oxd-input--active'])[4]").send_keys("100")
    # # time.sleep(5)
    # # switch
    # driver.find_element(By.XPATH,"(//span[@class='oxd-switch-input oxd-switch-input--active --label-right'])[1]").click()
    # time.sleep(5)
    # # save
    # driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    # time.sleep(5)

    # Add
    driver.find_element(By.XPATH, "//button[normalize-space()='Add']").click()
    time.sleep(5)
    # key performanze Indicator
    driver.find_element(By.XPATH, "(//input[@class='oxd-input oxd-input--active'])[2]").send_keys("Service")
    time.sleep(5)
    # job title
    driver.find_element(By.CSS_SELECTOR, ".oxd-select-text-input").click()
    time.sleep(5)
    driver.find_element(By.XPATH, "(//span[normalize-space()='Chief Executive Officer'])[1]").click()
    time.sleep(5)
    # Minimum rating
    driver.find_element(By.XPATH, "(//input[@modelmodifiers='[object Object]'])[1]").send_keys("80")
    time.sleep(5)
    # switch
    driver.find_element(By.XPATH,
                        "(//span[@class='oxd-switch-input oxd-switch-input--active --label-right'])[1]").click()
    time.sleep(5)
    # cancel
    driver.find_element(By.XPATH, "//button[normalize-space()='Cancel']").click()
    time.sleep(5)

    # configure
    driver.find_element(By.XPATH, "//span[normalize-space()='Configure']//i[@class='oxd-icon bi-chevron-down']").click()
    time.sleep(5)

    # trackers
    driver.find_element(By.XPATH, "//a[normalize-space()='Trackers']").click()
    time.sleep(5)

    # type for hints
    driver.find_element(By.XPATH, "//input[@placeholder='Type for hints...']").send_keys("pet")
    time.sleep(5)
    driver.find_element(By.XPATH, "//span[normalize-space()='Peter Mac Anderson']").click()
    time.sleep(5)
    # search
    # driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    # time.sleep(5)

    # Add
    # driver.find_element(By.XPATH, "//button[normalize-space()='Add']").click()
    # # tracker name
    # driver.find_element(By.XPATH, "(//input[@class='oxd-input oxd-input--active'])[2]").send_keys("Customer")
    # # employee name
    #
    # driver.find_element(By.XPATH, "(//input[@placeholder='Type for hints...'])[1]").send_keys("pet")
    # time.sleep(5)
    # driver.find_element(By.XPATH, "//span[normalize-space()='Peter Mac Anderson']").click()
    # time.sleep(5)
    # # reviwers
    # driver.find_element(By.XPATH, "(//input[@placeholder='Type for hints...'])[2]").send_keys("jo")
    # time.sleep(5)
    # driver.find_element(By.XPATH, "//span[contains(text(),'Joseph')]").click()
    # time.sleep(5)
    # driver.find_element(By.XPATH, "(//input[@placeholder='Type for hints...'])[2]").send_keys("ja")
    # time.sleep(5)
    # driver.find_element(By.XPATH, "//span[contains(text(),'James')]").click()
    # time.sleep(5)
    # driver.find_element(By.XPATH, "(//input[@placeholder='Type for hints...'])[2]").send_keys("ra")
    # time.sleep(5)
    # driver.find_element(By.XPATH, "//span[normalize-space()='Ravi M B']").click()
    # time.sleep(5)
    # # clear name
    # driver.find_element(By.XPATH, "(//i[@class='oxd-icon bi-x --clear'])[2]").click()
    # time.sleep(5)
    # # Save
    # driver.find_element(By.XPATH, "//button[normalize-space()='Save']").click()
    # time.sleep(5)
    #
    # # Add
    # driver.find_element(By.XPATH, "//button[normalize-space()='Add']").click()
    # time.sleep(5)
    # # cancel
    # driver.find_element(By.XPATH, "//button[normalize-space()='Cancel']").click()
    # time.sleep(5)
    # # scroll
    # scr = driver.find_element(By.XPATH, "//button[normalize-space()='Add']")
    # time.sleep(5)
    # driver.execute_script("arguments[0].scrollIntoView(true);", scr)
    # time.sleep(5)
    # # checkbox
    # checkbx = driver.find_element(By.XPATH, "(//i[@class='oxd-icon bi-check oxd-checkbox-input-icon'])[2]").click()
    # time.sleep(5)
    # # delete
    # driver.find_element(By.XPATH, "(//button[normalize-space()='Delete Selected'])[1]").click()
    # time.sleep(5)
    # driver.find_element(By.CSS_SELECTOR,
    #                     "button[class='oxd-button oxd-button--medium oxd-button--label-danger orangehrm-button-margin']").click()
    # time.sleep(5)
    # # checkbox
    #
    # check = driver.find_element(By.XPATH, "(//i[@class='oxd-icon bi-check oxd-checkbox-input-icon'])[2]").click()
    # time.sleep(5)
    # # delete
    # driver.find_element(By.XPATH, "(//button[normalize-space()='Delete Selected'])[1]").click()
    # time.sleep(5)
    # driver.find_element(By.XPATH, "//button[normalize-space()='No, Cancel']").click()
    # time.sleep(5)
    # # trash
    # driver.find_element(By.XPATH, "(//i[@class='oxd-icon bi-trash'])[2]").click()
    # time.sleep(5)
    # # yes delete
    # driver.find_element(By.CSS_SELECTOR,
    #                     "button[class='oxd-button oxd-button--medium oxd-button--label-danger orangehrm-button-margin']").click()
    # time.sleep(5)
    # # trash
    # driver.find_element(By.XPATH, "(//i[@class='oxd-icon bi-trash'])[2]").click()
    # time.sleep(5)
    # # no delete
    # driver.find_element(By.XPATH, "//button[normalize-space()='No, Cancel']").click()
    # time.sleep(5)
    # # trash
    # driver.find_element(By.XPATH, "(//i[@class='oxd-icon bi-trash'])[2]").click()
    # time.sleep(5)
    # # close
    # driver.find_element(By.XPATH, "//button[normalize-space()='×']").click()
    # time.sleep(5)
    #
    # # pencil
    # driver.find_element(By.XPATH, "(//i[@class='oxd-icon bi-pencil-fill'])[2]").click()
    # time.sleep(5)
    # # edit performance tracker
    # tracker = driver.find_element(By.XPATH, "(//input[@class='oxd-input oxd-input--active'])[2]")
    # time.sleep(5)
    # tracker.send_keys(Keys.BACKSPACE * 8)
    # time.sleep(5)
    # tracker.send_keys("customer")
    # time.sleep(5)
    # # employee name
    # emp = driver.find_element(By.XPATH, "(//input[@placeholder='Type for hints...'])[1]")
    # time.sleep(5)
    # emp.send_keys(Keys.BACKSPACE * 18)
    # time.sleep(5)
    # emp.send_keys("em")
    # time.sleep(5)
    # driver.find_element(By.XPATH, "//span[contains(text(),'Emily')]").click()
    # time.sleep(5)
    # # close a element
    # driver.find_element(By.XPATH, "(//i[@class='oxd-icon bi-x --clear'])[2]").click()
    # time.sleep(5)
    # # save
    # driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    # time.sleep(5)
    # # scroll
    # scr = driver.find_element(By.XPATH, "//button[normalize-space()='Add']")
    # time.sleep(5)
    # driver.execute_script("arguments[0].scrollIntoView(true);", scr)
    # time.sleep(5)
    # # pencil
    # driver.find_element(By.XPATH, "(//i[@class='oxd-icon bi-pencil-fill'])[2]").click()
    # time.sleep(5)
    # # cancel
    # driver.find_element(By.XPATH, "//button[normalize-space()='Cancel']").click()
    # time.sleep(5)
    # # reset
    # driver.find_element(By.XPATH, "//button[normalize-space()='Reset']").click()
    # time.sleep(5)
    #
    # # employee Review
    # driver.find_element(By.XPATH, "//span[normalize-space()='Manage Reviews']").click()
    # time.sleep(5)
    # driver.find_element(By.XPATH, "//a[normalize-space()='Employee Reviews']").click()
    # time.sleep(5)
    #
    # # employee name
    # driver.find_element(By.CSS_SELECTOR, "input[placeholder='Type for hints...']").send_keys("pet")
    # time.sleep(5)
    # driver.find_element(By.XPATH, "//span[text()='Peter Mac Anderson']").click()
    # time.sleep(5)
    # # job title
    # driver.find_element(By.CSS_SELECTOR, ".oxd-select-text-input").click()
    # time.sleep(5)
    # driver.find_element(By.XPATH, "//span[text()='Chief Executive Officer']").click()
    # time.sleep(5)
    # #  sub unit
    # driver.find_element(By.XPATH,
    #                     "(//div[@class='oxd-select-text-input'][normalize-space()='-- Select --'])[2]").click()
    # time.sleep(5)
    # driver.find_element(By.XPATH, "(//span[normalize-space()='Quality Assurance'])[1]").click()
    # time.sleep(5)
    # # review status
    # driver.find_element(By.XPATH, "//div[@clear='false']").click()
    # time.sleep(5)
    # driver.find_element(By.XPATH, "(//span[normalize-space()='Completed'])[1]").click()
    # time.sleep(5)
    # # calendar
    # # from date
    # driver.find_element(By.XPATH, "(//input[@placeholder='yyyy-dd-mm'])[1]").click()
    # time.sleep(5)
    # driver.find_element(By.XPATH, "(//div[@class='oxd-calendar-date'][normalize-space()='3'])[1]").click()
    # time.sleep(5)
    # # to date
    # driver.find_element(By.XPATH, "(//input[@placeholder='yyyy-dd-mm'])[2]")
    # time.sleep(5)
    # driver.find_element(By.XPATH, "(//div[contains(text(),'4')])[4]")
    # time.sleep(5)
    # # include
    # driver.find_element(By.CSS_SELECTOR, ".oxd-icon.bi-caret-up-fill.oxd-select-text--arrow").click()
    # time.sleep(5)
    # driver.find_element(By.XPATH, "//span[normalize-space()='Current and Past Employees']").click()
    # time.sleep(5)
    # # search
    # driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    # time.sleep(5)
    # # reset
    # driver.find_element(By.CSS_SELECTOR, "button[type='reset']").click()
    # time.sleep(5)
    #
    # # My review
    # driver.find_element(By.XPATH, "//span[normalize-space()='Manage Reviews']").click()
    # time.sleep(5)
    # driver.find_element(By.XPATH, "//a[normalize-space()='My Reviews']").click()
    # time.sleep(5)
    # driver.find_element(By.XPATH, "(//i[@class='oxd-icon bi-file-text-fill'])[1]").click()
    # time.sleep(5)
    # # scroll
    # kpi = driver.find_element(By.XPATH, "(//p[normalize-space()='Self Evaluation by'])[1]")
    # driver.execute_script("arguments[0].scrollIntoView(true);", kpi)
    # time.sleep(5)
    # # text field
    # driver.find_element(By.XPATH, "(//input)[2]").send_keys("70")
    # time.sleep(5)
    # driver.find_element(By.XPATH, "(//textarea)[1]").send_keys("Average")
    # time.sleep(5)
    #
    # driver.find_element(By.XPATH, "(//input)[3]").send_keys("80")
    # time.sleep(5)
    # driver.find_element(By.XPATH, "(//textarea)[2]").send_keys("Good")
    # time.sleep(5)
    #
    # driver.find_element(By.XPATH, "(//input)[4]").send_keys("75")
    # time.sleep(5)
    # driver.find_element(By.XPATH, "(//textarea)[3]").send_keys("Not bad")
    # time.sleep(5)
    #
    # driver.find_element(By.XPATH, "(//input)[5]").send_keys("90")
    # time.sleep(5)
    # driver.find_element(By.XPATH, "(//textarea)[4]").send_keys("very good")
    # time.sleep(5)
    #
    # driver.find_element(By.XPATH, "(//input)[6]").send_keys("95")
    # time.sleep(5)
    # driver.find_element(By.XPATH, "(//textarea)[5]").send_keys("Excellant")
    # time.sleep(5)
    # # scroll
    # abc = driver.find_element(By.XPATH, "//p[@title='Succession Plans in Place']")
    # driver.execute_script("arguments[0].scrollIntoView(true);", abc)
    # time.sleep(5)
    # # general comment
    # # driver.find_element(By.XPATH,"//textarea[@class='oxd-textarea oxd-textarea--focus oxd-textarea--resize-vertical orangehrm-evaluation-grid-comment']").send_keys("Overall performance is Good")
    # # time.sleep(5)
    # # element = WebDriverWait(driver, 10).until(
    # #          EC.presence_of_element_located((By.XPATH, "(//textarea[@class='oxd-textarea oxd-textarea--active oxd-textarea--resize-vertical orangehrm-evaluation-grid-comment'])[6]"))
    # #     )
    # # time.sleep(5)
    # # save
    # driver.find_element(By.XPATH, "//button[normalize-space()='Save']").click()
    # time.sleep(5)
    # # scroll
    # kpi = driver.find_element(By.XPATH, "(//p[normalize-space()='Self Evaluation by'])[1]").click()
    # time.sleep(5)
    # driver.execute_script("arguments[0].scrollIntoView(true);", kpi)
    # time.sleep(5)
    # # scroll
    # abc = driver.find_element(By.XPATH, "//p[@title='Succession Plans in Place']")
    # driver.execute_script("arguments[0].scrollIntoView(true);", abc)
    # # cancel
    # driver.find_element(By.XPATH, "//button[normalize-space()='Cancel']").click()
    # time.sleep(5)
    # driver.find_element(By.XPATH, "(//i[@class='oxd-icon bi-file-text-fill'])[1]").click()
    # time.sleep(5)
    # # complete
    # driver.find_element(By.XPATH, "//button[normalize-space()='Complete']").click()
    # time.sleep(5)
    # # cancel
    # driver.find_element(By.XPATH,
    #                     "(//button[@class='oxd-button oxd-button--medium oxd-button--ghost orangehrm-button-margin'])[1]").click()
    # time.sleep(5)
    # # complete
    # driver.find_element(By.XPATH, "//button[normalize-space()='Complete']").click()
    # time.sleep(5)
    # # close
    # driver.find_element(By.XPATH, "//button[normalize-space()='×']").click()
    # time.sleep(5)
    # # complete
    # driver.find_element(By.XPATH, "//button[normalize-space()='Complete']").click()
    # time.sleep(5)
    # # ok
    # driver.find_element(By.CSS_SELECTOR, "//button[normalize-space()='Ok']").click()
    # time.sleep(5)
    #
    # # Manager review
    # driver.find_element(By.XPATH, "//span[normalize-space()='Manage Reviews']").click()
    # time.sleep(5)
    # driver.find_element(By.XPATH, "//a[normalize-space()='Manage Reviews']").click()
    # time.sleep(5)
    #
    # # driver.find_element(By.XPATH,"//span[normalize-space()='Manage Reviews']").click()
    # # time.sleep(5)
    # # driver.find_element(By.XPATH,"//a[normalize-space()='Manage Reviews']").click()
    # # time.sleep(5)
    #
    # # employee name
    # driver.find_element(By.CSS_SELECTOR, "input[placeholder='Type for hints...']").send_keys("1")
    # time.sleep(5)
    # driver.find_element(By.XPATH, "//span[text()='Clay August Macejkovic']").click()
    # time.sleep(5)
    # # job title
    # driver.find_element(By.CSS_SELECTOR, ".oxd-select-text-input").click()
    # time.sleep(5)
    # driver.find_element(By.XPATH, "//span[text()='Chief Executive Officer']").click()
    # time.sleep(5)
    # #  sub unit
    # driver.find_element(By.XPATH,
    #                     "(//div[@class='oxd-select-text-input'][normalize-space()='-- Select --'])[2]").click()
    # time.sleep(5)
    # driver.find_element(By.XPATH, "(//span[normalize-space()='Quality Assurance'])[1]").click()
    # time.sleep(5)
    # # review status
    # driver.find_element(By.XPATH, "//div[@clear='false']").send_keys("1")
    # time.sleep(5)
    # driver.find_element(By.XPATH, "//span[text()='Clay August Macejkovic']").click()
    # time.sleep(5)
    # # calendar
    # # from date
    # driver.find_element(By.XPATH, "(//input[@placeholder='yyyy-dd-mm'])[1]").click()
    # time.sleep(5)
    # driver.find_element(By.XPATH, "(//div[@class='oxd-calendar-date'][normalize-space()='3'])[1]").click()
    # time.sleep(5)
    # # to date
    # driver.find_element(By.XPATH, "(//input[@placeholder='yyyy-dd-mm'])[2]")
    # time.sleep(5)
    # driver.find_element(By.XPATH, "(//div[contains(text(),'4')])[4]")
    # time.sleep(5)
    # # include
    # driver.find_element(By.CSS_SELECTOR, ".oxd-icon.bi-caret-up-fill.oxd-select-text--arrow").click()
    # time.sleep(5)
    # driver.find_element(By.XPATH, "//span[normalize-space()='Current and Past Employees']").click()
    # time.sleep(5)
    # # search
    # driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    # time.sleep(5)
    # # scroll
    # checkb = driver.find_element(By.XPATH, "//button[normalize-space()='Add']")
    # driver.execute_script("arguments[0].scrollIntoView(true);", checkb)
    # # checkbox
    # checkboxes = driver.find_element(By.XPATH, "(//i[@class='oxd-icon bi-check oxd-checkbox-input-icon'])[1]").click()
    # time.sleep(5)
    #
    # # add
    # driver.find_element(By.XPATH, "//button[normalize-space()='Add']").click()
    # # employee name
    # driver.find_element(By.XPATH, "(//input[@placeholder='Type for hints...'])[1]").send_keys("1")
    # time.sleep(5)
    # driver.find_element(By.XPATH, "//span[normalize-space()='Clay August Macejkovic']").click()
    # time.sleep(5)
    # # supervisor review
    # driver.find_element(By.XPATH, "(//input[@placeholder='Type for hints...'])[2]").send_keys("James")
    # time.sleep(5)
    # # Review Period Start Date
    # driver.find_element(By.XPATH, "(//i[@class='oxd-icon bi-calendar oxd-date-input-icon'])[1]").click()
    # time.sleep(5)
    # driver.find_element(By.XPATH, "(//div[@class='oxd-calendar-date'][normalize-space()='1'])[1]").click()
    # time.sleep(5)
    # # Review Period End Date
    # driver.find_element(By.XPATH, "(//i[@class='oxd-icon bi-calendar oxd-date-input-icon'])[2]").click()
    # time.sleep(5)
    # driver.find_element(By.XPATH, "(//div[contains(text(),'12')])[2]").click()
    # time.sleep(5)
    # # Due Date
    # driver.find_element(By.XPATH, "(//i[@class='oxd-icon bi-calendar oxd-date-input-icon'])[3]").click()
    # time.sleep(5)
    # driver.find_element(By.XPATH, "(//div[contains(text(),'18')])[3]").click()
    # time.sleep(5)
    # # Save
    # driver.find_element(By.XPATH, "//button[normalize-space()='Save']").click()
    # time.sleep(5)
    # # activate
    # driver.find_element(By.XPATH, "//button[normalize-space()='Activate']").click()
    # time.sleep(5)
    # # cancel
    # driver.find_element(By.XPATH, "//button[normalize-space()='Cancel']").click()
    # time.sleep(5)
    # # reset
    # driver.find_element(By.CSS_SELECTOR, "button[type='reset']").click()
    # time.sleep(5)

def manage(self,browser):
    driver = browser
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    self.test_perfor(driver)