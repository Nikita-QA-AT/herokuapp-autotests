from selenium.webdriver.common.by import By

def test_add_button(driver):
    driver.get("https://the-internet.herokuapp.com/add_remove_elements/")
    button_add_element = driver.find_element(By.CSS_SELECTOR, "button").click()