import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



def test_product_card_page (browser):
    """
    Предусловие: в корзине нет товаров
    Тест: Поиск элементов
    1) Найдем значение которое отображается "в корзине" перед началом теста
    2) Найдем цену товара
    3) Найдем количество товара
    4) Найдем и кликнем по кнопке Add to cart
    5) Найдем новое значение "в корзине"
    """
    browser.get(browser.url + "/iphone")
    browser.implicitly_wait(60)
    #1)найдем значение которое отображается "в корзине" перед началом теста
    cart_total_before = browser.find_element(By.CSS_SELECTOR, "#cart-total").text
    assert "0 item(s) - $0.00" in cart_total_before

    #2)найдем цену товара
    product_price_float = float(browser.find_element(By.CSS_SELECTOR,"li:nth-child(1) > h2").text.replace('$', ''))

    #3)найдем количество товара
    product_qty = int(browser.find_element(By.CSS_SELECTOR, "#input-quantity").get_attribute("value"))

    #4)найдем и кликнем по кнопке Add to cart
    browser.find_element(By.CSS_SELECTOR, "#button-cart").click()
    time.sleep(0.5)

    #5)проверим новое значение "в корзине"
    cart_total_after = browser.find_element(By.CSS_SELECTOR, "#cart-total").text
    assert cart_total_before != cart_total_after
    expected_cart_btn_value = str(product_qty) + " item(s) - $" + str(format(product_qty * product_price_float,'.2f'))
    assert cart_total_after == expected_cart_btn_value
