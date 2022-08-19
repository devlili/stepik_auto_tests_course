from selenium.webdriver.common.by import By
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_should_see_the_add_to_cart_button(browser):
    browser.get(link)
    time.sleep(30)
    button = browser.find_elements(By.CSS_SELECTOR, "button.btn.btn-lg.btn-primary")
    assert button, "button is not find"
