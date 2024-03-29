from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import cmd

def calc(x):#функция для вычисления y
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html83333")

# говорим Selenium проверять в течение 12 секунд, пока значение элемента price не будет равнно 100
WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"),"100"))

button = browser.find_element_by_id("book")  # находим кнопку
button.click()

x_element = browser.find_element_by_id("input_value")  # находим элемент где в тексте находится атрибут со значением
x = x_element.text  # получаем значени х из текста и передаем в переменную
y = calc(int(x))  # находим y

input1 = browser.find_element_by_id("answer")
input1.send_keys(str(y))  # вставляем у в найденное поле

button = browser.find_element_by_id("solve")  # находим кнопку
button.click()
