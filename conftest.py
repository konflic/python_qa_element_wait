import pytest
import logging

from selenium import webdriver

logging.basicConfig(level=logging.DEBUG)

@pytest.fixture
def browser(request):
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    request.addfinalizer(driver.close)
    return driver
