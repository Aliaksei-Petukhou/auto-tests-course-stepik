import math
import os 
#def calc(x):
#  return str(math.log(abs(12*math.sin(int(x)))))
from selenium import webdriver
import time

try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    #x_element = browser.find_element_by_css_selector('#input_value')
    #x = x_element.text
    #y = calc(x)
    
    # Ваш код, который заполняет обязательные поля
    #time.sleep(1)
    input1 = browser.find_element_by_css_selector('[name="firstname"]')
    input1.send_keys("Alexei")
    #time.sleep(1)
    input2 = browser.find_element_by_css_selector('[name="lastname"]')
    input2.send_keys("Petukhou")
    input3 = browser.find_element_by_css_selector('[name="email"]')
    input3.send_keys("paftor@ya.ru")
    #input2 = browser.find_element_by_css_selector('[type="checkbox"]')
    #input2.click()
    #time.sleep(1)
    #input3 = browser.find_element_by_css_selector('[for="robotsRule"]')
    #browser.execute_script("return arguments[0].scrollIntoView(true);", input3)
    #time.sleep(2)
    #input3.click()
    
    input4 = browser.find_element_by_css_selector('[type="file"]')
    
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'name.txt')           # добавляем к этому пути имя файла 
    input4.send_keys(file_path)

    # Отправляем заполненную форму
    
    #button = browser.find_element_by_tag_name("button")
    
   
    
    button = browser.find_element_by_css_selector('[type="submit"]')
    #browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    #time.sleep(2)
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    #time.sleep(3)
    
    #welcome_text_elt = browser.find_element_by_xpath('//p[contains(text(), "for 2020")]')
    #welcome_text = welcome_text_elt.text
    #assert "Lesson for 2020-01-19" == welcome_text

    #input4 = browser.find_element_by_css_selector('.name a')
    #input4.click()
    #time.sleep(3)
    #input5 = browser.find_element_by_css_selector('[data-text="Log Out"]')
    #input5.click()
    #time.sleep(3)
    # находим элемент, содержащий текст
    #//p[contains(text(), "cat")]
   

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()