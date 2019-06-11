import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from steps.constants.constants import EXPLICIT_WAIT_SECS

def wait_for_expected_title(driver, desired_title):
    try:
        element = WebDriverWait(driver, EXPLICIT_WAIT_SECS).until(
            EC.title_contains(desired_title)
        )
        additional_safer_wait(2)
    except TimeoutException as e:
        pass

def click_and_wait_for_navigation(driver, xpath):
    try:
        web_element = driver.find_element_by_xpath(xpath)
        if web_element.is_displayed():
            driver.find_element_by_xpath(xpath).click()
            
            # to check if the element is invisible.
            element = WebDriverWait(driver, EXPLICIT_WAIT_SECS).until_not(
                EC.presence_of_element_located(
                    (By.XPATH, xpath)
                )
            )
            additional_safer_wait(2)
    except:
        pass

def additional_safer_wait(wait_seconds):
    time.sleep(int(wait_seconds))