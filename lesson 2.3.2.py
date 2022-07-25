from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("http://suninjuly.github.io/redirect_accept.html")

button = driver.find_element(By.CSS_SELECTOR, "button.btn")
button.click()

driver.switch_to.window(driver.window_handles[1])

find_element = driver.find_element(By.ID, "input_value")
x_element = find_element.text
x = int(x_element)
y = calc(x)

input1 = driver.find_element(By.ID, "answer")
input1.send_keys(y)
button = driver.find_element(By.CSS_SELECTOR, "button.btn")
button.click()

print(driver.switch_to.alert.text)
driver.quit()
