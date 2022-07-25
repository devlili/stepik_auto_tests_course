from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("http://suninjuly.github.io/get_attribute.html")

find_element = driver.find_element(By.ID, "treasure")
x_element = find_element.get_attribute("valuex")
x = x_element
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
