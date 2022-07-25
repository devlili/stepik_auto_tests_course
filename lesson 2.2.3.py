from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("http://SunInJuly.github.io/execute_script.html")

find_element = driver.find_element(By.ID, "input_value")
x_element = find_element.text
x = int(x_element)
y = calc(x)

input1 = driver.find_element(By.ID, "answer")
input1.send_keys(y)
option1 = driver.find_element(By.ID, "robotCheckbox")
option1.click()
driver.execute_script("window.scrollBy(0, 100);")
option2 = driver.find_element(By.ID, "robotsRule")
option2.click()
button = driver.find_element(By.CSS_SELECTOR, "button.btn")
button.click()

time.sleep(10)
driver.quit()
