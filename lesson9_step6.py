from selenium import webdriver
import time
import math

def calc(x):#функция для вычисления y
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_css_selector("button.btn")#находим кнопку
    button.click()

    window_name = browser.window_handles[1]
    browser.switch_to.window(window_name)

    x_element = browser.find_element_by_id("input_value")#находим элемент где в тексте находится атрибут со значением
    x = x_element.text  #получаем значени х из текста и передаем в переменную
    y = calc(int(x))#находим y

    input1 = browser.find_element_by_id("answer")
    input1.send_keys(str(y))#вставляем у в найденное поле

    button = browser.find_element_by_css_selector("button.btn")#находим кнопку
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла