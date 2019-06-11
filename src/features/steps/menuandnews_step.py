import random
import time
import easygui
from behave import given,when,then
from selenium import webdriver

from steps.locators.web_elements import *
from steps.constants import constants
from steps.utils.wait_handlers import click_and_wait_for_navigation
import steps.utils.helper as Helper

@given("the Skynews webpage is successfully opened")
def verify_page_load(context):
    assert context.config.userdata.get('url') in context.driver.current_url

@when("the homepage contents are displayed in the application")
def verify_home_page_header(context):
    displayed_header_text =  context.driver.find_element_by_xpath(HOME_PAGE_HEADER).text
    expected_header_text =  constants.HOME_PAGE_HEADER
    assert displayed_header_text.strip().lower() == expected_header_text.strip().lower()

@then("the browser's tab title should be as expected")
def verify_browser_title(context):
    assert context.driver.title == constants.HOME_TITLE_TEXT

@given("the Skynews webpage is opened, verify the browser's tab title")
def verify_home_page(context):
    assert context.config.userdata.get('url') in context.driver.current_url

    displayed_header_text =  context.driver.find_element_by_xpath(HOME_PAGE_HEADER).text
    expected_header_text =  constants.HOME_PAGE_HEADER
    assert displayed_header_text.strip().lower() == expected_header_text.strip().lower()

    assert context.driver.title == constants.HOME_TITLE_TEXT

@when("the number of menu categories and names are displayed as expected")
@then("the number of menu categories and names are displayed as expected")
def verify_categories(context):
    category_element = context.driver.find_element_by_xpath(MENU_CATEGORIES)
    category_list = category_element.find_elements_by_tag_name("li")
    
    # Validating the menu items count
    category_count = len(category_list)
    assert category_count == constants.CATEGORY_COUNT

    # Validating if the desired menu list are displayed
    for category in category_list:
        if category.text != '':
            category_text = category.text
            assert category_text.strip() in constants.CATEGORY_LIST
        else:
            break

@when("the {menu_name} menu category is selected")
def select_menu_category(context, menu_name):
    Helper.select_menu_category(context.driver, menu_name)

@then("verify if the default focus point is on the {menu_name} Category")
@then("the focus point should be changed to {menu_name}")
def verify_focus_point(context, menu_name):
    focus_tab_text = Helper.get_current_focus_tab(context.driver)
    assert focus_tab_text.strip() == menu_name.strip()

@when("the {news_tile_number} news story is selected from the list of stories")
def story_title_match(context, news_tile_number):

    # Extracting number from string. Eg: 2nd -> 2
    news_tile_number = ''.join([n for n in news_tile_number if n.isdigit()])

    # dynamically changing the xpath
    tile_xpath = SAMPLE_NEWS_TILE.replace('REPLACE_TILE_NUMBER', news_tile_number)
    tile_text_xpath = SAMPLE_NEWS_TILE_TEXT.replace('REPLACE_TILE_NUMBER', news_tile_number)

    news_tile_element = context.driver.find_element_by_xpath(tile_xpath)

    #Scrolling to the element in order to gain visibility
    context.driver.execute_script("arguments[0].scrollIntoView();", news_tile_element)
    time.sleep(5)

    if news_tile_element.is_displayed():
        context.news_tile_text = context.driver.find_element_by_xpath(tile_text_xpath).text
    else:
        raise Exception('The excpected tile is not displayed in the application.')

    click_and_wait_for_navigation(context.driver, tile_xpath)

@then("the navigated page should have the news title text appropriately")
def verify_news_tile_navigation(context):
    if context.driver.find_element_by_xpath(NEWS_TITLE).is_displayed():

        # Picks a word of random choice
        tile_words_split = context.news_tile_text.split()
        picked_word_position = random.randint(0, len(tile_words_split)-1)

        #Verifies if the picked word is displayed in the navigated page
        assert tile_words_split[picked_word_position] in context.driver.find_element_by_xpath(NEWS_TITLE).text
        assert tile_words_split[picked_word_position] in context.driver.title
    else:
        raise Exception('The news tile page navigation failed.')
