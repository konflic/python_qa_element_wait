def test_disabled_button(browser):
    browser.get("https://konflic.github.io/front_example/pages/shadow.html")

    # Так не сработает
    # button = browser.find_element("css selector", "#button")
    # button.click()

    # Используем js
    # def shadow_element(element):
    #     shadow_root = browser.execute_script('return arguments[0].shadowRoot', element)
    #     return shadow_root
    #
    # shadow = shadow_element(browser.find_element_by_css_selector("#elem"))
    # inner = shadow.find_element_by_css_selector("#button")
    # inner.click()

    assert browser.find_element_by_css_selector("body > div").text == "SHADOW!"
