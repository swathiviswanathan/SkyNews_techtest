Feature: To test the SkyNews webpage navigations, menu and other features.

    @skynews_techtest   @Verify_browser_tab_title   @functional
    Scenario: Verify the Sky News browser tab title
        Given the Skynews webpage is successfully opened
        When the homepage contents are displayed in the application
        Then the browser's tab title should be as expected

    @skynews_techtest   @Verify_menu_categories     @functional
    Scenario: Verify the Sky News categories count and names
        Given the Skynews webpage is successfully opened
        When the homepage contents are displayed in the application
        Then the number of menu categories and names are displayed as expected

    @skynews_techtest   @Verify_focus_point     @functional
    Scenario: Verify the webpage's category focus point changes
        Given the Skynews webpage is successfully opened
        When the homepage contents are displayed in the application
        Then verify if the default focus point is on the Home Category
        When the Ocean Rescue menu category is selected
        Then the focus point should be changed to Ocean Rescue

    @skynews_techtest   @Verify_story_selection     @functional
    Scenario: Verify the Sky News categories count and names
        Given the Skynews webpage is successfully opened
        When the 5th news story is selected from the list of stories
        Then the navigated page should have the news title text appropriately

    @skynews_techtest   @regression     @verify_news_complete_navigation
    Scenario Outline: Verify the category navigation and news tile navigation features of SkyNews Webpage.
        Given the Skynews webpage is opened, verify the browser's tab title
        When the number of menu categories and names are displayed as expected
        Then verify if the default focus point is on the Home Category
        When the Ocean Rescue menu category is selected
        Then the focus point should be changed to Ocean Rescue
        When the Home menu category is selected
        Then the focus point should be changed to Home
        When the <NewsTileNumber> news story is selected from the list of stories
        Then the navigated page should have the news title text appropriately

        Examples:
        | NewsTileNumber |
        | 3rd            |
        | 1st            |
        | 4th            |
        | 5th            |
        | 2nd            |