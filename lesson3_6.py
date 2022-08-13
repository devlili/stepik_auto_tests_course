import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    browser.quit()


@pytest.mark.parametrize('links', ['236895', '236896', '236897', '236898', '236899', '236903', '236904', '236905'])
def test_find_text(browser, links):
    browser.get(f"https://stepik.org/lesson/{links}/step/1")
    browser.implicitly_wait(13)
    browser.find_element(By.CSS_SELECTOR, ".textarea.ember-text-area").send_keys(str(math.log(int(time.time() + 2.2))))
    button = WebDriverWait(browser, 8).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.submit-submission")))
    button.click()
    message = WebDriverWait(browser, 8).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".smart-hints__hint"))).text
    assert "Correct!" == message, "Should be write the word 'Correct'"
    print(message)

if __name__ == "__main__":
    pytest.main()
