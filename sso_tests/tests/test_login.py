# tests/test_login.py
from pages.login_page import LoginPage

def test_valid_login(driver):
    page = LoginPage(driver)
    page.open()
    page.set_phone("+79000000000")
    page.set_password("ValidPass123")
    page.click_login()
    assert "redirect" in driver.current_url

def test_invalid_login(driver):
    page = LoginPage(driver)
    page.open()
    page.set_phone("+79000000000")
    page.set_password("InvalidPass")
    page.click_login()
    assert page.get_error_message() == "Неверный логин или пароль"

