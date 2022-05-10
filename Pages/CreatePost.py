from Pages.Locators import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
# https://community.powerbi.com/t5/Data-Stories-Gallery/Meat-to-eat-or-not-to-eat-Narrative-statistics/td-p/2177919s

class CreatePost:
    def __init__(self, driver):
        self.driver = driver

    def check_main_page(self):
        self.driver.find_element(By.LINK_TEXT, create_a_post_button_link_text).click()

    def enter_title(self, title):
        self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div[2]/div/div/div/div[2]/div/div[1]/div[1]/input').send_keys(title)

    def select_source(self):
        self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div[2]/div/div/div/div[2]/div/div[1]/div[2]/select').Select()


