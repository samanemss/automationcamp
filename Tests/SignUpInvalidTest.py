from Pages.SignUp import SignUp
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
import unittest
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


class SignUpTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.service = Service(executable_path=ChromeDriverManager().install())
        cls.options = Options()
        cls.options.headless = True
        cls.driver = webdriver.Chrome(service=cls.service, options=cls.options)
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_invalid_signup(self):
        self.driver.get("https://sharedataset.com/account/login")
        signup = SignUp(driver=self.driver)
        signup.signup_link()
        signup.enter_email("samane_mss@yahoo.com")
        signup.enter_password_signup("123456S@vdash")
        signup.continue_button_name_signup()
        signup.wrong_alert()

        sleep(20)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()
        cls.driver.quit()


sleep(20)
