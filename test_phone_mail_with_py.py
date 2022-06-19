# print -  просто для себя отследить этапы работы теста
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


link = "http://www.google.ru"
company = "Byndyusoft"


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


class TestContacts():
   # вызываем фикстуру в тесте, передав ее как параметр
    def test_search_phone(self, browser):
        print("start test1")
        browser.get(link)
        search_box = browser.find_element(By.TAG_NAME, 'input')  # найти поисковую строку
        search_box.send_keys(company)  # ввести искомое слово в поисковую строку
        search_box.send_keys(Keys.RETURN)  # имитация нажатия Enter
        browser.find_element(By.PARTIAL_LINK_TEXT, company).click()  # найти ссылку по части имени
        new_window = browser.window_handles[1]  # нашли новую вкладку
        browser.switch_to.window(new_window)  # перешли на новую вкладку
        # найти кнопку "заказать презентацию", клик
        browser.find_element(By.CLASS_NAME, 'btn.btn--lg.btn--info.js-popup-callback-show').click()
        phone = browser.find_element(By.XPATH, "//*[contains(@class, 'popup-callback__footer-contacts')]/a[@ href='tel:88007751521']")
        phone_text = phone.text
        print("телефон:", phone_text)
        assert phone_text == "8 800 775-15-21", "Номер телефона не соответствет ожидаемому результату"
        print("finish test1")

    def test_search_email(self, browser):
        print("start test2")
        browser.get(link)
        search_box = browser.find_element(By.TAG_NAME, 'input')  # найти поисковую строку
        search_box.send_keys(company)  # ввести искомое слово в поискову строку
        search_box.send_keys(Keys.RETURN)  # имитация нажатия Enter
        browser.find_element(By.PARTIAL_LINK_TEXT, company).click()  # найти ссылку по части имени
        new_window = browser.window_handles[1]  # нашли новую вкладку
        browser.switch_to.window(new_window)  # перешли на новую вкладку
        # найти кнопку "заказать презентацию"
        browser.find_element(By.CLASS_NAME, 'btn.btn--lg.btn--info.js-popup-callback-show').click()
        email = browser.find_element(By.XPATH, "//*[contains(@class, 'popup-callback__footer-contacts')]/a[@ href='mailto:sales@byndyusoft.com']")
        email_text = email.text  # взять текст найденного элемента
        print("электронная почта:", email_text)
        assert email_text == "sales@byndyusoft.com", "Адрес электронной почты не соответствет ожидаемому результату"
        print("finish test2")
