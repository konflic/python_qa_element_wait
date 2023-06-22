from selenium import webdriver

firefox = webdriver.Firefox()
firefox.get("https://yandex.ru")

home_tabs = firefox.find_element(value="text")

# Получаем значение свойства innerHTML
html = home_tabs.get_property("innerHTML")
print(html)

# Получаем значение свойства data-bem
attr = home_tabs.get_attribute("data-bem")
print(attr)

# Получаем значение CSS войства margin-bottom
css = home_tabs.value_of_css_property("margin-bottom")
print(css)

firefox.close()
