from Pages.Locators import *
from selenium.webdriver.common.by import By



class SignUp:
    def __init__(self, driver):
        self.driver = driver

    def enter_email(self, email):
        self.driver.find_element('id', email_textbox_id).send_keys(email)

    def enter_password_signup(self, password):
        self.driver.find_element('id', password_textbox_id_signup).send_keys(password)

    def continue_button_name_signup(self):
        self.driver.find_element('name', continue_button_name_signup).click()

    def signup_link(self):
        self.driver.find_element(By.LINK_TEXT, signup_link_text).click()

    def wrong_alert(self):
        self.driver.find_element('id', wrong_alert_id)

    def main_page(self):
        self.driver.find_element(By.LINK_TEXT, create_a_post_button_link_text)
