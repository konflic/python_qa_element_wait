import time

from locators import MainPage, CatalogPage
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains


def test_select_value(browser):
    browser.get("https://demo.opencart.com/")
    desktops_link = browser.find_element(*MainPage.DESKTOPS)

    time.sleep(2)
    ActionChains(browser).move_to_element(desktops_link).pause(2).perform()
    browser.find_element(*MainPage.SHOW_ALL).click()
    select_limit = Select(browser.find_element(*CatalogPage.SELECT_LIMIT))

    time.sleep(2)
    select_limit.select_by_visible_text("100")
    select_limit = Select(browser.find_element(*CatalogPage.SELECT_LIMIT))
    assert select_limit.first_selected_option.text == "100"

    time.sleep(2)
    select_limit.select_by_visible_text("50")
    select_limit = Select(browser.find_element(*CatalogPage.SELECT_LIMIT))
    assert select_limit.first_selected_option.text == "50"
