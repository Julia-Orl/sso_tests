# tests/test_recovery.py
from pages.recovery_page import RecoveryPage


def test_password_recovery_by_phone(driver):
    page = RecoveryPage(driver)
    page.open()
    page.set_username("+79000000000")
    page.click_continue()
    page.select_sms_option()
    page.click_send_code()

    # Предположим, что код приходит на экран (например, через API или фейковый)
    code = "123456"
    page.enter_code(code)

    new_password = "NewPass123"
    page.set_new_password(new_password)
    page.set_confirm_password(new_password)
    page.click_save()

    # Проверяем, что мы перешли на страницу авторизации
    assert "auth" in driver.current_url, "Пароль не был изменен"


def test_recovery_with_mismatched_passwords(driver):
    page = RecoveryPage(driver)
    page.open()
    page.set_username("+79000000000")
    page.click_continue()
    page.select_sms_option()
    page.click_send_code()

    code = "123456"
    page.enter_code(code)

    page.set_new_password("NewPass123")
    page.set_confirm_password("WrongPass123")
    page.click_save()

    error = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//span[contains(text(), 'Пароли не совпадают')]"))
    )
    assert error.is_displayed(), "Ошибка о несовпадении паролей не отображена"
  
