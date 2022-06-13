

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

 
try:
    link = "http://www.google.ru"  # open google.ru
    browser = webdriver.Chrome()
    browser.get(link)

    
    searchBox = browser.find_element(By.TAG_NAME, 'input')  # найти поисковую строку
    searchBox.send_keys('Byndyusoft')  # ввести искомое слово в поискову строку
    searchBox.send_keys(Keys.RETURN)  # имитация нажатия Enter
        
    browser.find_element(By.PARTIAL_LINK_TEXT, 'Byndyusoft').click()  # locate by partial link and open Byndyusoft

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    
    browser.find_element(By.CLASS_NAME, 'btn.btn--lg.btn--info.js-popup-callback-show').click()
    
    # если искомый элемент перекрыт другим другим элементом
    # button = browser.find_element(By.CLASS_NAME, 'btn.btn--lg.btn--info.js-popup-callback-show')
    # browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    # button.click()
    

    phone = browser.find_element(By.XPATH, "//a[@ href='tel:88007751521']")
    phone_text = phone.text
    assert phone_text == "8 800 775-15-21", "Номер телефона не соответствет ожидаемому результату"


    email = browser.find_element(By.XPATH, "//a[@ href='mailto:sales@byndyusoft.com']")
    email_text = email.text
    assert email_text == "sales@byndyusoft.com", "Адрес электронной почты не соответствет ожидаемому результату"

    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта    
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
