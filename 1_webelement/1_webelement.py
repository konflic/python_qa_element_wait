from selenium import webdriver

chrome = webdriver.Chrome()

chrome.get("https://yandex.ru")

# search_input это объект типа WebElement
search_input = chrome.find_element_by_css_selector("input#text")

chrome.close()
