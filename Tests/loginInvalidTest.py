from Pages.Login import Login
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
import unittest
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


class LoginTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.service = Service(executable_path=ChromeDriverManager().install())
        cls.options = Options()
        cls.options.headless = True
        cls.driver = webdriver.Chrome(service=cls.service, options=cls.options)
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_invalid_login(self):
        self.driver.get("https://sharedataset.com/account/login")
        login = Login(driver=self.driver)

        login.enter_username("samane.mss@yahoo.com")
        login.enter_password("123456S@dash")
        login.click_on_continue_button()
        login.wrong_email_password()

        sleep(30)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()
        cls.driver.quit()


sleep(20)
