from Pages.Locators import *
from selenium.webdriver.common.by import By


class MainPage:
    def __init__(self, driver):
        self.driver = driver

    def check_main_page(self):
        self.driver.find_element(By.LINK_TEXT, create_a_post_button_link_text)

