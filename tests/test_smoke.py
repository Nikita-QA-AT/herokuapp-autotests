def test_open_main_page(driver):
    driver.get("https://the-internet.herokuapp.com")
    header = driver.find_element("tag name", "h1").text
    assert "Welcome to the-internet" in header