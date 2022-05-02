from Pages.Login import Login
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from time import sleep
from Pages.MainPage import MainPage
import unittest


class LoginTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.service = Service(executable_path=ChromeDriverManager().install())
        cls.driver = webdriver.Chrome(service=cls.service)
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_valid_login(self):
        self.driver.get("https://sharedataset.com/account/login")
        login = Login(driver=self.driver)
        main_page = MainPage(driver=self.driver)
        login.enter_username("samane_mss@yahoo.com")
        login.enter_password("123456S@vdash")
        login.click_on_continue_button()
        main_page.check_main_page()
        sleep(30)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()
        cls.driver.quit()


sleep(5)
