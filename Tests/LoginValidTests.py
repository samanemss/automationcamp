from Pages.Login import Login
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from time import sleep
from Pages.MainPage import MainPage
import unittest
from selenium.webdriver.chrome.options import Options


class LoginTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.service = Service(executable_path=ChromeDriverManager().install())
        cls.options = Options()
        cls.options.headless = True
        cls.driver = webdriver.Chrome(service=cls.service, options=cls.options)
        cls.driver.implicitly_wait(3)
        cls.driver.maximize_window()

    def test_valid_login(self):
        self.driver.get("https://sharedataset.com/account/login")
        login = Login(driver=self.driver)
        main_page = MainPage(driver=self.driver)
        login.enter_username("samane_mss@yahoo.com")
        login.enter_password("123456S@vdash")
        login.click_on_continue_button()
        main_page.check_main_page()

        sleep(20)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()
        cls.driver.quit()


sleep(5)
