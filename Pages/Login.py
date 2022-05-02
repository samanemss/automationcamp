from Pages.Locators import *


class Login:
    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, username):
        self.driver.find_element('id', username_textbox_id).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element('id', password_textbox_id).send_keys(password)

    def click_on_continue_button(self):
        self.driver.find_element('name', continue_button_name).click()

    def wrong_email_password(self):
        self.driver.find_element('id', wrong_email_password_id)
