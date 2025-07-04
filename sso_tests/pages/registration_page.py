# pages/registration_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class RegistrationPage:
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get("https://lk.rt.ru/account/register ")

    def set_first_name(self, name):
        self.driver.find_element(By.NAME, "firstName").send_keys(name)

    def set_last_name(self, surname):
        self.driver.find_element(By.NAME, "lastName").send_keys(surname)

    def set_email_or_phone(self, value):
        self.driver.find_element(By.ID, "address").send_keys(value)

    def set_password(self, password):
        self.driver.find_element(By.ID, "password").send_keys(password)

    def set_confirm_password(self, password):
        self.driver.find_element(By.ID, "password-confirm").send_keys(password)

    def click_register(self):
        self.driver.find_element(By.NAME, "register").click()

    def get_error_message(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//span[@data-error='registration_credentials']"))
        ).text

    def is_password_match_error(self):
        error = self.driver.find_element(By.XPATH, "//span[contains(text(), 'Пароли не совпадают')]")
        return error.is_displayed()

    def is_email_already_used(self):
        return "Email уже используется" in self.get_error_message()

