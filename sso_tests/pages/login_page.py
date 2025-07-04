# pages/login_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get("https://lk.rt.ru/ ")

    def set_username(self, username):
        self.driver.find_element(By.ID, "username").send_keys(username)

    def set_password(self, password):
        self.driver.find_element(By.ID, "password").send_keys(password)

    def click_login(self):
        self.driver.find_element(By.ID, "kc-login").click()

    def get_error_message(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//span[@data-error='login_credentials']"))
        ).text

    def is_redirect(self):
        return "redirect" in self.driver.current_url

    def change_to_email_tab(self):
        self.driver.find_element(By.XPATH, "//div[contains(text(), 'Почта')]").click()

    def change_to_phone_tab(self):
        self.driver.find_element(By.XPATH, "//div[contains(text(), 'Номер')]").click()

    def change_to_account_tab(self):
        self.driver.find_element(By.XPATH, "//div[contains(text(), 'Лицевой счет')]").click()

    def is_forgot_password_orange(self):
        forgot_pass = self.driver.find_element(By.LINK_TEXT, "Забыл пароль")
        return "orange" in forgot_pass.value_of_css_property("color")