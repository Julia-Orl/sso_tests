# pages/login_page.py
class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get("https://lk.rt.ru/ ")

    def set_phone(self, phone):
        self.driver.find_element("id", "username").send_keys(phone)

    def set_password(self, password):
        self.driver.find_element("id", "password").send_keys(password)

    def click_login(self):
        self.driver.find_element("id", "kc-login").click()

    def get_error_message(self):
        return self.driver.find_element("xpath", "//span[@data-error='login_credentials']").text
