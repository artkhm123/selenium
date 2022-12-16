import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config import *


def test_incorrect_login_message(browser):
    """
    Тест: Поверка наличия элементов
    1) заголовок "Please enter your login details."
    2) блок о не верных данных "No match for Username and/or Password" - отсутствует
    3) найдем поле username. введем в него не валидное значение
    4) найдем поле password. введем в него не валидное значение
    5) найдем кнопку login. кликнем по ней
    6) блок о не верных данных "No match for Username and/or Password" - появился
    """
    browser.get(browser.url + "/admin")
    WebDriverWait(browser, 2).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#content")))
    # 1) заголовок "Please enter your login details."
    h1 = browser.find_element(By.CSS_SELECTOR, "h1.panel-title")
    assert "Please enter your login details." in h1.text

    # 2) блок о неверных данных "No match for Username and/or Password" - отсутствует
    assert len(browser.find_elements(By.PARTIAL_LINK_TEXT, "No match for Username and/or Password")) == 0

    # 3) найдем поле username. введем в него не валидное значение
    username_field = browser.find_element(By.CSS_SELECTOR, "#input-username")
    username_field.clear()
    username_field.send_keys(NON_EXISTING_USERNAME)

    # 4) найдем поле password. введем в него не валидное значение
    password_field = browser.find_element(By.CSS_SELECTOR, "#input-password")
    password_field.clear()
    password_field.send_keys(WRONG_PASSWORD)

    # 5) найдем кнопку login. кликнем по ней
    WebDriverWait(browser,2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))
    browser.find_element(By.CSS_SELECTOR, "button[type=submit]").click()

    # 6) блок о не верных данных "No match for Username and/or Password" - появился
    WebDriverWait(browser, 2).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".alert.alert-danger.alert-dismissible")))
    alert_message_after_click = browser.find_elements(By.CSS_SELECTOR, ".alert.alert-danger.alert-dismissible")
    assert len(alert_message_after_click) > 0
    assert "No match for Username and/or Password." in alert_message_after_click[0].text
