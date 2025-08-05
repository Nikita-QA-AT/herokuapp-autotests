from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

def test_add_button(driver):
    # открыли страницу
    driver.get("https://the-internet.herokuapp.com/add_remove_elements/")


    # кликнули по кнопке Add element 1 раз
    WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button"))
    ).click()

    # кликнули по кнопке Add element 2 раз
    WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button"))
    ).click()

    # кликнули по кнопке Add element 3 раз
    WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button"))
    ).click()
    time.sleep(1)

    # нашли все кнопки delete
    delete_buttons = driver.find_elements(By.CSS_SELECTOR, ".added-manually")
    assert len(delete_buttons) == 3


    # проверили, что появилась кнопка delete
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#elements .added-manually"))
    )

    # Проверяем текст кнопки
    button_delete = driver.find_element(By.CSS_SELECTOR, ".added-manually")
    assert button_delete.text == "Delete"

    for btn in delete_buttons:
        btn.click()
        time.sleep(1)
    test push from work computer
