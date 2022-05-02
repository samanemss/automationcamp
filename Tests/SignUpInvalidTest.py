from Pages.SignUp import SignUp
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
import unittest


class SignUpTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        cls.driver.implicitly_wait(5)
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
