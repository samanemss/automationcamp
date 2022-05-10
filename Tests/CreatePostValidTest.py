from Pages.Login import Login
from Pages.CreatePost import CreatePost
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from time import sleep
from Pages.MainPage import MainPage
import unittest
from selenium.webdriver.chrome.options import Options


class CreatePostTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.service = Service(executable_path=ChromeDriverManager().install())
        cls.options = Options()
        cls.options.headless = False
        cls.driver = webdriver.Chrome(service=cls.service, options=cls.options)
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_valid_createpost(self):
        self.driver.get("https://sharedataset.com/account/login")
        login = Login(driver=self.driver)
        login.enter_username("samane_mss@yahoo.com")
        login.enter_password("123456S@vdash")
        login.click_on_continue_button()
        main_page = CreatePost(driver=self.driver)
        main_page.check_main_page()
        main_page.enter_title("Test")
        main_page.select_source_powerbi()
        main_page.enter_publicurl("https://community.powerbi.com/t5/Data-Stories-Gallery/Meat-to-eat-or-not-to-eat-Narrative-statistics/td-p/2177919")
        main_page.enter_originalauthor("a9126030767")
        main_page.enter_description("Test")
        main_page.enter_tags("Test")
        main_page.select_whocanseepost()
        main_page.enter_license("Test")
        main_page.enter_uploadposter()
        main_page.submitpost()

        sleep(10)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()
        cls.driver.quit()


sleep(10)
