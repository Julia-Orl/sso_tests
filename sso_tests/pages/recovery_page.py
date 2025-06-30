# pages/recovery_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class RecoveryPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://lk.rt.ru/auth/realms/rtkc/account/password/reset "

    def open(self):
        self.driver.get(self.url)

    def set_username(self, username):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "username"))
        ).send_keys(username)

    def click_continue(self):
        self.driver.find_element(By.XPATH, "//button[contains(text(), 'Далее')]").click()

    def select_sms_option(self):
        self.driver.find_element(By.XPATH, "//input[@value='sms']").click()

    def click_send_code(self):
        self.driver.find_element(By.XPATH, "//button[contains(text(), 'Получить код повторно')]").click()

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
        return self.driver.find_element(By.XPATH, "//span[@data-error='login_credentials']").text

