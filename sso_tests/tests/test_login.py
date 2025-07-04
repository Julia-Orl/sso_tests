# tests/test_login.py
from pages.login_page import LoginPage

import pytest
from pages.login_page import LoginPage


def test_valid_login_by_phone(driver):
    page = LoginPage(driver)
    page.open()
    page.set_username("+79000000000")
    page.set_password("ValidPass123")
    page.click_login()
    assert page.is_redirect(), "Не произошел редирект после входа"


def test_invalid_login_by_phone(driver):
    page = LoginPage(driver)
    page.open()
    page.set_username("+79000000000")
    page.set_password("InvalidPass")
    page.click_login()
    assert page.get_error_message() == "Неверный логин или пароль", "Ошибка авторизации не отображена"
    assert page.is_forgot_password_orange(), "Кнопка 'Забыл пароль' не окрасилась в оранжевый"


def test_login_with_empty_phone(driver):
    page = LoginPage(driver)
    page.open()
    page.change_to_phone_tab()
    page.set_username("")
    page.set_password("ValidPass123")
    page.click_login()
    assert "необходимо заполнить это поле" in page.get_error_message(), "Ошибка пустого поля не отображена"


def test_login_by_email(driver):
    page = LoginPage(driver)
    page.open()
    page.change_to_email_tab()
    page.set_username("valid@example.com")
    page.set_password("ValidPass123")
    page.click_login()
    assert page.is_redirect(), "Не произошел редирект при авторизации через email"


def test_login_by_account_number(driver):
    page = LoginPage(driver)
    page.open()
    page.change_to_account_tab()
    page.set_username("LS1234567890")
    page.set_password("ValidPass123")
    page.click_login()
    assert page.is_redirect(), "Не произошел редирект при авторизации по лицевому счету"


def test_login_with_13_digits_in_phone(driver):
    page = LoginPage(driver)
    page.open()
    page.set_username("+790000000000")
    page.set_password("ValidPass123")
    page.click_login()
    assert "Введите телефон в формате +7XXXXXXXXXX" in page.get_error_message(), "Ошибка невалидного телефона не отображена"


def test_login_with_special_chars_in_phone(driver):
    page = LoginPage(driver)
    page.open()
    page.set_username("+7(900)000-00-00")
    page.set_password("ValidPass123")
    page.click_login()
    assert "Введите телефон в формате +7XXXXXXXXXX" in page.get_error_message(), "Ошибка ввода спецсимволов не отображена"


def test_login_with_cyrillic_password(driver):
    page = LoginPage(driver)
    page.open()
    page.set_username("+79000000000")
    page.set_password("Пароль123")
    page.click_login()
    assert "Пароль должен содержать только латинские буквы" in page.get_error_message(), "Ошибка ввода кириллицы не отображена"

