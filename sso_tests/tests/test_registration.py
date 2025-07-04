# test_registration.py
import pytest
from pages.registration_page import RegistrationPage


def test_register_with_existing_email(driver):
    page = RegistrationPage(driver)
    page.open()
    page.set_first_name("Иван")
    page.set_last_name("Иванов")
    page.set_email_or_phone("existing@example.com")
    page.set_password("ValidPass123")
    page.set_confirm_password("ValidPass123")
    page.click_register()
    assert page.is_email_already_used(), "Система не проверяет уникальность email"


def test_register_with_invalid_email_format(driver):
    page = RegistrationPage(driver)
    page.open()
    page.set_first_name("Петр")
    page.set_last_name("Петров")
    page.set_email_or_phone("invalid-email@")
    page.set_password("ValidPass123")
    page.set_confirm_password("ValidPass123")
    page.click_register()
    assert "Некорректный email" in page.get_error_message(), "Система не проверяет формат email"


def test_register_with_less_than_2_letters_in_name(driver):
    page = RegistrationPage(driver)
    page.open()
    page.set_first_name("A")
    page.set_last_name("B")
    page.set_email_or_phone("newuser@example.com")
    page.set_password("ValidPass123")
    page.set_confirm_password("ValidPass123")
    page.click_register()
    assert "минимум 2 символа" in page.get_error_message(), "Система не проверяет длину имени"


def test_register_with_non_latin_password(driver):
    page = RegistrationPage(driver)
    page.open()
    page.set_first_name("Анна")
    page.set_last_name("Иванова")
    page.set_email_or_phone("anna@example.com")
    page.set_password("пароль123")
    page.set_confirm_password("пароль123")
    page.click_register()
    assert "Пароль должен содержать только латинские буквы" in page.get_error_message(), "Система не проверяет язык пароля"
