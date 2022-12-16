import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_catalog_page(browser):
    """
    Тест: Поиск элементов
    1) Поиск и переход в раздел Desktops через блок категорий слева
    2) Поиск заголовка выбранной категориии
    3) Поиск выбранной категории в бредкрамбах
    4) Поиск и выбор подкатегории
    5) Поиск выбранной подкатегории в бредкрамбах
    6) Поиск изображения продукта на продуктовой тумбе
    """
    browser.get(browser.url + "/component")
    WebDriverWait(browser, 2).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#product-category")))

    #1) Поиск и переход в раздел Desktops через блок категорий слева
    WebDriverWait(browser, 3).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#column-left")))
    aside_block = browser.find_element(By.CSS_SELECTOR, "#column-left")
    WebDriverWait(browser, 3).until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, "#column-left > div > a[href='http://192.168.31.28:8081/desktops']")))
    aside_block.find_element(By.PARTIAL_LINK_TEXT, "Desktops").click()

    #2) Поиск заголовка выбранной категориии Desktops
    WebDriverWait(browser, 2).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#content")))
    assert "Desktops" in browser.find_element(By.CSS_SELECTOR, "h2").text

    #3) Поиск выбранной категории в бредкрамбах
    WebDriverWait(browser, 1).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".breadcrumb")))
    breadrcumbs_state_desktops = browser.find_elements(By.CSS_SELECTOR, ".breadcrumb > li")
    assert "Desktops" in breadrcumbs_state_desktops[1].text

    # 4) Поиск и выбор подкатегории Mac
    WebDriverWait(browser, 3).until(EC.visibility_of_element_located((By.CSS_SELECTOR,"#column-left")))
    monitors = browser.find_element(By.CSS_SELECTOR,"#column-left > div > a[href='http://192.168.31.28:8081/desktops/mac']")
    monitors.click()


    # 5) Поиск выбранной подкатегории в бредкрамбах
    WebDriverWait(browser, 1).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".breadcrumb")))
    breadrcumbs_state_mac = browser.find_elements(By.CSS_SELECTOR, ".breadcrumb > li")
    assert "Desktops" in breadrcumbs_state_mac[1].text
    assert "Mac" in breadrcumbs_state_mac[2].text

    # 6) Поиск первого в списке продукта и поиск картинки на продуктовой тумбе
    WebDriverWait(browser, 3).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".product-thumb")))
    first_product = browser.find_elements(By.CSS_SELECTOR, ".product-thumb")[0]
    first_product_img = first_product.find_element(By.TAG_NAME, "img")
