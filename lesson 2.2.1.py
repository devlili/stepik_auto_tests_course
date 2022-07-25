from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("http://suninjuly.github.io/selects1.html")

find_x = driver.find_element(By.ID, "num1")
x = find_x.text
find_y = driver.find_element(By.ID, "num2")
y = find_y.text
sum = int(x) + int(y)
select = Select(driver.find_element(By.CSS_SELECTOR, "select.custom-select"))
select.select_by_value(str(sum))

button = driver.find_element(By.CSS_SELECTOR, "button.btn")
button.click()

time.sleep(15)
driver.quit()
