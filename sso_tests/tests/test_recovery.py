# tests/test_recovery.py
import pytest
from pages.recovery_page import RecoveryPage


def test_password_recovery_by_email(driver):
    page = RecoveryPage(driver)
    page.open()
    page.set_username("test@example.com")
    page.click_continue()
    page.select_email_option()
    code = "123456"
    page.enter_code(code)
    new_password = "NewPass123"
    page.set_new_password(new_password)
    page.set_confirm_password(new_password)
    page.click_save()
    assert "redirect" in driver.current_url, "Пароль не был изменен"


def test_recovery_with_mismatched_passwords(driver):
    page = RecoveryPage(driver)
    page.open()
    page.set_username("test@example.com")
    page.click_continue()
    page.select_email_option()
    code = "123456"
    page.enter_code(code)
    page.set_new_password("NewPass123")
    page.set_confirm_password("WrongPass123")
    page.click_save()
    assert page.is_password_match_error(), "Ошибка о несовпадении паролей не отображена"


def test_recovery_with_expired_code(driver):
    page = RecoveryPage(driver)
    page.open()
    page.set_username("+79000000000")
    page.click_continue()
    page.select_sms_option()
    code = "000000"
    page.enter_code(code)
    assert "Время жизни кода истекло" in page.get_error_message(), "Ошибка истекшего кода не отображена"


def test_recovery_with_reused_password(driver):
    page = RecoveryPage(driver)
    page.open()
    page.set_username("+79000000000")
    page.click_continue()
    page.select_sms_option()
    code = "123456"
    page.enter_code(code)
    page.set_new_password("OldPass123")
    page.set_confirm_password("OldPass123")
    page.click_save()
    assert "Этот пароль уже использовался" in page.get_policy_error(), "Старый пароль принят системой"