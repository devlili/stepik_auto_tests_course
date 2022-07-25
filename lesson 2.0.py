from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("http://suninjuly.github.io/math.html")

x_element = driver.find_element(By.ID, "input_value")
x = x_element.text
y = calc(x)
input1 = driver.find_element(By.ID, "answer")
input1.send_keys(y)
option1 = driver.find_element(By.ID, "robotCheckbox")
option1.click()
option2 = driver.find_element(By.ID, "robotsRule")
option2.click()
button = driver.find_element(By.CSS_SELECTOR, "button.btn")
button.click()

time.sleep(15)
driver.quit()
