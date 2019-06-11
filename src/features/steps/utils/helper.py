from steps.locators.web_elements import *

from steps.constants import constants
from steps.utils.wait_handlers import wait_for_expected_title

def get_current_focus_tab(driver):
    return driver.find_element_by_xpath(CURRENT_FOCUS_MENU).text

def select_menu_category(driver, desired_menu_item):
    try:
        menu_categories = driver.find_element_by_xpath(MENU_CATEGORIES)
        menu_list = menu_categories.find_elements_by_tag_name("li")
        for menu_item in menu_list:
            if menu_item.text.strip() == desired_menu_item:
                menu_item.click()
                break
        
        if desired_menu_item == 'Home':
            wait_for_expected_title(driver, constants.HOME_TITLE_TEXT)
        else:
            wait_for_expected_title(driver, desired_menu_item)
    except:
        pass
