# pages/recovery_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class RecoveryPage:
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get("https://lk.rt.ru/auth/realms/rtkc/account/password/reset ")

    def set_username(self, username):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "username"))
        ).send_keys(username)

    def click_continue(self):
        self.driver.find_element(By.XPATH, "//button[contains(text(), 'Далее')]").click()

    def select_sms_option(self):
        self.driver.find_element(By.XPATH, "//input[@value='sms']").click()

    def select_email_option(self):
        self.driver.find_element(By.XPATH, "//input[@value='email']").click()

    def enter_code(self, code):
        fields = self.driver.find_elements(By.XPATH, "//input[@type='text']")
        for i in range(len(code)):
            fields[i].send_keys(code[i])

    def set_new_password(self, password):
        self.driver.find_element(By.ID, "password").send_keys(password)

    def set_confirm_password(self, password):
        self.driver.find_element(By.ID, "password-confirm").send_keys(password)

    def click_save(self):
        self.driver.find_element(By.XPATH, "//button[contains(text(), 'Сохранить')]").click()

    def get_error_message(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//span[@data-error='login_credentials']"))
        ).text

    def get_policy_error(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//span[contains(text(), 'Длина пароля должна быть не менее 8 символов')]"))
        ).text

    def is_password_too_short(self):
        return "Длина пароля должна быть не менее 8 символов" in self.get_policy_error()

    def is_password_missing_uppercase(self):
        return "Пароль должен содержать хотя бы одну заглавную букву" in self.get_policy_error()

    def is_password_non_latin(self):
        return "Пароль должен содержать только латинские буквы" in self.get_policy_error()
