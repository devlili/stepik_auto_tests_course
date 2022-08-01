from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".card-body #price"), "$100")
    )

button1 = browser.find_element(By.CSS_SELECTOR, "button#book")
button1.click()

find_element = browser.find_element(By.ID, "input_value")
x_element = find_element.text
x = int(x_element)
y = calc(x)

input1 = browser.find_element(By.ID, "answer")
input1.send_keys(y)
button2 = browser.find_element(By.CSS_SELECTOR, "button#solve")
button2.click()

print(browser.switch_to.alert.text)
browser.quit()
