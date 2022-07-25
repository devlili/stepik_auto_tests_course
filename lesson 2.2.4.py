from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import os

link = "http://suninjuly.github.io/file_input.html"
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(link)

try:
    input1 = driver.find_element(By.NAME, "firstname")
    input1.send_keys("Ivan")
    input2 = driver.find_element(By.NAME, "lastname")
    input2.send_keys("Petrov")
    input3 = driver.find_element(By.NAME, "email")
    input3.send_keys("1111@ya.ru")
    element = driver.find_element(By.ID, "file")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'text.txt')  # добавляем к этому пути имя файла
    element.send_keys(file_path)

    button = driver.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    time.sleep(1)

finally:
    time.sleep(15)
    driver.quit()

