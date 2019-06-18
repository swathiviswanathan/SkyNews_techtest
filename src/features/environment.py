from selenium import webdriver
import time
import sys

from steps.utils.wait_handlers import click_and_wait_for_navigation

from steps.locators.web_elements import AGREE_PRIVACY
def before_all(context):

    dirname = os.path.dirname(__file__)
    
    browser = context.config.userdata.get('browser')
    if browser.lower() == 'safari':
        context.driver = webdriver.Safari()
    elif browser.lower() == 'ie' and sys.platform == 'win32':
        ie_driver = os.path.join(dirname, context.config.userdata.get('ie_driver_path'))
        context.driver = webdriver.Ie(ie_driver)
    elif browser.lower() == 'firefox':
        driver_path = context.config.userdata.get('gecko_driver_path', None)
        if driver_path is not None:
            firefox_driver = os.path.join(dirname, driver_path)
            context.driver = webdriver.Firefox(executable_path=firefox_driver)
        else:
            context.driver = webdriver.Firefox()
    elif browser.lower() == 'chrome':
        driver_path = context.config.userdata.get('chrome_driver_path', None)
        options = webdriver.ChromeOptions()
        if driver_path is not None:
            options.binary_location = os.path.join(dirname, driver_path)

        context.driver = webdriver.Chrome(chrome_options=options)
    else:
        raise Exception(
            'Unknown/unmatching browser platform specified. please pick from safari/chrome/firefox/ie')

def before_scenario(context, scenario):
    context.driver.get(context.config.userdata.get('url'))
    context.driver.maximize_window()
    click_and_wait_for_navigation(context.driver, AGREE_PRIVACY)

def after_all(context):
    context.driver.quit()
