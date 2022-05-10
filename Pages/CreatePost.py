from Pages.Locators import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class CreatePost:
    def __init__(self, driver):
        self.driver = driver

    def check_main_page(self):
        self.driver.find_element(By.LINK_TEXT, create_a_post_button_link_text).click()

    def enter_title(self, title):
        self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div[2]/div/div/div/div[2]/div/div[1]/div[1]/input').send_keys(title)

    def select_source_powerbi(self):
        source = self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div[2]/div/div/div/div[2]/div/div[1]/div[2]/select')
        drop = Select(source)
        drop.select_by_value("powerbi")

    def enter_publicurl(self, publicurl):
        self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div[2]/div/div/div/div[2]/div/div[1]/div[3]/input').send_keys(publicurl)

    def enter_originalauthor(self, originalauthor):
        self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div[2]/div/div/div/div[2]/div/div[1]/div[4]/input').send_keys(originalauthor)

    def enter_description(self, descriptions):
        self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div[2]/div/div/div/div[2]/div/div[1]/div[5]/textarea').send_keys(descriptions)

    def enter_tags(self, tags):
        self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div[2]/div/div/div/div[2]/div/div[1]/div[6]/input').send_keys(tags)

    def select_whocanseepost(self):
        seepost = self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div[2]/div/div/div/div[2]/div/div[1]/div[7]/select')
        dropseepost = Select(seepost)
        dropseepost.select_by_value("private")

    def enter_license(self, license):
        self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div[2]/div/div/div/div[2]/div/div[1]/div[8]/input').send_keys(license)

    def enter_uploadposter(self):
        self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div[2]/div/div/div/div[2]/div/div[2]/div[2]/input').send_keys('C:/Users/samaneh/Pictures/Saved Pictures/OIP.jpg')

    def submitpost(self):
        self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div[2]/div/div/div/div[3]/button').click()



