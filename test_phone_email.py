from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
#import time


link = "http://www.google.ru"
company = 'Byndyusoft'

class TestPhoneEmail:
    try:
        browser = webdriver.Chrome()   # open google.ru
        browser.get(link)

        try:
            searchBox = browser.find_element(By.TAG_NAME, 'input')  # найти поисковую строку
            searchBox.send_keys(company)  # ввести искомое слово в поискову строку
            searchBox.send_keys(Keys.RETURN)  # имитация нажатия Enter
        except Exception:
            print("не найден searchBox. Тест провален")
            browser.quit()

        try:
            browser.find_element(By.PARTIAL_LINK_TEXT, company).click()  #  найти первую ссылку и кликнуть
            new_window = browser.window_handles[1]
            browser.switch_to.window(new_window)  #  перейти на другую вкладку
        except Exception:
            print("не найден new_window. Тест провален")
            browser.quit()
    
        try:
            browser.find_element(By.CLASS_NAME, 'btn.btn--lg.btn--info.js-popup-callback-show').click()  # кнопка 'заказать презентацию'
        except Exception:
            print("кнопка 'заказать презентацию' не найдена или не нажата. Тест провален")
            browser.quit()
  
        try:
            phone = browser.find_element(By.XPATH, "//*[contains(@class, 'popup-callback__footer-contacts')]/a[@ href='tel:88007751521']")  # сверить номер телефона
            phone_text = phone.text
        except Exception:
            print("не найден phone. Тест провален")
            browser.quit()
        assert phone_text == "8 800 775-15-21", "Номер телефона не соответствет ожидаемому результату"
            
        try:
            email = browser.find_element(By.XPATH, "//*[contains(@class, 'popup-callback__footer-contacts')]/a[@ href='mailto:sales@byndyusoft.com']")
            email_text = email.text  # сверить email
        except Exception:
            print("не найден email. Тест провален")
            browser.quit()
        assert email_text == "sales@byndyusoft.com", "Адрес электронной почты не соответствет ожидаемому результату"
        
        print(f"Тест пройден до конца. Номер телефона: {phone_text}  и email: {email_text} - соответсвуют ожидаемому.")
       
    finally:
        # закрываем браузер после всех манипуляций
        browser.quit()
    
        
  