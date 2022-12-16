
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_main_page_elements(browser):
    """
    Тест: Проверка наличия элементов:
    1) продуктовые тумбы - 4 шт
    2) в каждой продуктовой тумбе есть :
    - кнопка Add to cart
    - кнопка Add to wishlist
    - кнопка Compare this product
    3) при клике на "compare this product" появляется блок "Success: You have added #название_продукта to your product comparison!"

    """
    browser.get(browser.url)

    #1)проверка что продуктовых тумбы 4шт
    WebDriverWait(browser, 2).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".row")))
    product_tumb_list = browser.find_elements(By.CSS_SELECTOR, ".product-thumb.transition")
    assert len(product_tumb_list) == 4

    #2)проверка что у каждой тумбы есть кнопки "Add to cart", "Compare this product", "Add to wishlist"
    for tumb in product_tumb_list:
        add_to_cart_btn = tumb.find_element(By.CSS_SELECTOR, "button[onclick*='cart']")
        comparison_btn = tumb.find_element(By.CSS_SELECTOR,"button[onclick*='wishlist']")
        wish_list_btn = tumb.find_element(By.CSS_SELECTOR,"button[onclick*='compare']")

    #3)проверка что при клике на "compare this product" появляется блок "Success: You have added #название_продукта to your product comparison!"
    for tumb in product_tumb_list:
        WebDriverWait(tumb, 2).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button[onclick*='compare']")))
        comparison_btn = tumb.find_element(By.CSS_SELECTOR, "button[onclick*='compare']")
        position_name_in_tumb = tumb.find_element(By.TAG_NAME, "h4").text
        comparison_btn.click()
        WebDriverWait(browser, 2).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".alert.alert-success.alert-dismissible")))
        success_block = browser.find_element(By.CSS_SELECTOR, ".alert.alert-success.alert-dismissible").text
        expected_success_block = "Success: You have added " + position_name_in_tumb + " to your product comparison!"
        assert expected_success_block in success_block
        close = browser.find_element(By.CSS_SELECTOR, "button[data-dismiss='alert']")
        close.click()
