import pytest
from selenium import webdriver


@pytest.fixture
def browser(request):
    driver = webdriver.Chrome()
    request.addfinalizer(driver.close)
    return driver
