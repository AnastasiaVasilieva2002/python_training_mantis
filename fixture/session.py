from selenium.webdriver.common.by import By
import time

class SessionHelper:

    def __init__(self, app):
        self.app = app


    def login(self, username, password):
        wd = self.app.wd
        time.sleep(2)
        self.app.open_home_page()
        wd.set_window_size(945, 1020)
        wd.find_element(By.NAME, "username").click()
        wd.find_element(By.NAME, "username").send_keys(username)
        wd.find_element(By.NAME, "password").click()
        wd.find_element(By.NAME, "password").send_keys(password)
        wd.find_element(By.CSS_SELECTOR, 'input[type="submit"]').click()

    def logout(self):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "Logout").click()

    def ensure_logout(self):
        wd = self.app.wd
        if self.is_logged_in():
            self.logout()

    def is_logged_in(self):
        wd = self.app.wd
        return len(wd.find_elements(By.LINK_TEXT, "Logout")) > 0

    def is_logged_in_as(self, username):
        wd = self.app.wd
        return self.get_logged_user() == username

    def get_logged_user(self):
        wd = self.app.wd
        return wd.find_element(By.CSS_SELECTOR, "td.login-info-left span").text

    def ensure_login(self, username, password):
        wd = self.app.wd
        if self.is_logged_in():
            if self.is_logged_in_as(username):
                return
            else:
                self.logout()
        self.login(username, password)