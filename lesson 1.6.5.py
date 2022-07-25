from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

try:
    link = "http://suninjuly.github.io/registration2.html"
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(link)

    input1 = driver.find_element(By.CLASS_NAME, "form-control.first:required")
    input1.send_keys("Ivan")
    input2 = driver.find_element(By.CLASS_NAME, "form-control.second:required")
    input2.send_keys("Petrov")
    input3 = driver.find_element(By.CLASS_NAME, "form-control.third:required")
    input3.send_keys("1111@ya.ru")

    # Отправляем заполненную форму
    button = driver.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = driver.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    driver.quit()