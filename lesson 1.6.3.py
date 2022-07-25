from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("http://suninjuly.github.io/huge_form.html")

elements = driver.find_elements(By.TAG_NAME, "input")
for element in elements:
    element.send_keys("Мой ответ")

button = driver.find_element(By.CSS_SELECTOR, "button.btn")
button.click()

time.sleep(15)
driver.quit()

# не забываем оставить пустую строку в конце файла