import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import *


def test_register_page(browser):
    """
    Тест: Поиск элементов
    1) Заголовк "Register Account", проверка цвета и размера его шрифта
    2) Найдем и вводем валидные данные в поля:
    -Firstname,
    -Lastname,
    -E-Mail,
    -Telephone,
    -Password,
    -Password Confirm
    3) Найдем ссылку Privat policy. Кликнем по ней
    4) Найдем заглавие модального окна
    5) Найдем кнопку закрытия модального окна и кликнем по ней

    """
    browser.get(browser.url+"/index.php?route=account/register")
    WebDriverWait(browser, 2).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#content")))

    #1)проверка заголовка "Register Account" текста, цвета и размера его шрифта
    h1 = browser.find_element(By.CSS_SELECTOR, "#content > h1")
    assert "Register Account" in h1.text
    assert h1.value_of_css_property("color") == H1_FONT_COLOR
    assert int(h1.value_of_css_property("font-size").replace('px', '')) == H1_FONT_SIZE

    #2)Найдем и вводем валидные данные в поля firstname, lastname, E-Mail, Telephone, Password, Password Confirm
    firstname_field = browser.find_element(By.CSS_SELECTOR, "#input-firstname")
    firstname_field.clear()
    firstname_field.send_keys(FIRSTNAME_NEW)
    lastname_field = browser.find_element(By.CSS_SELECTOR, "#input-lastname")
    lastname_field.clear()
    lastname_field.send_keys(LASTNAME_NEW)
    email_field = browser.find_element(By.CSS_SELECTOR, "#input-email")
    email_field.clear()
    email_field.send_keys(EMAIL_NEW)
    phone_field = browser.find_element(By.CSS_SELECTOR, "#input-telephone")
    phone_field.clear()
    phone_field.send_keys(PHONE_NEW)
    password_field = browser.find_element(By.CSS_SELECTOR, "#input-password")
    password_field.clear()
    password_field.send_keys(PASSWORD)
    confirm_password_field = browser.find_element(By.CSS_SELECTOR, "#input-confirm")
    confirm_password_field.clear()
    confirm_password_field.send_keys(PASSWORD)

    #3)Найдем ссылку Privat policy. Кликнем по ней
    account_reg_form = browser.find_element(By.CSS_SELECTOR, "#account-register")
    account_reg_form.find_element(By.LINK_TEXT, "Privacy Policy").click()

    # Дождемся пока откроется модальное окно и найдем заглавие модального окна
    WebDriverWait(browser, 2).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".modal-dialog")))
    assert "Privacy Policy" in browser.find_element(By.CSS_SELECTOR, "h4.modal-title").text

    #5) Найдем кнопку закрытия модального окна и кликнем по ней -> модальное окно закрыто
    browser.find_element(By.CSS_SELECTOR, "button.close").click()
    WebDriverWait(browser, 2).until(EC.presence_of_element_located((By.CSS_SELECTOR, "body[class='']")))
    assert browser.find_element(By.CSS_SELECTOR, "#modal-agree").get_attribute('style') == "display: none;"
