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

        def test_valid_createpost_powerbi(self):
            self.driver.get("https://sharedataset.com/account/login")
            login = Login(driver=self.driver)
            login.enter_username("samane_mss@yahoo.com")
            login.enter_password("123456S@vdash")
            login.click_on_continue_button()
            main_page = CreatePost(driver=self.driver)
            main_page.check_main_page()
            main_page.enter_title("Test_PowerBI_OnlyMe")
            main_page.select_source_powerbi()
            main_page.enter_publicurl(
                "https://app.powerbi.com/view?r=eyJrIjoiZDIxOTgwOGQtNmNlOS00NTJmLWE2NWUtYzU4ZWNkOWI0MTFjIiwidCI6IjkyNWJkNTViLTA1MjEtNDAwMy1iN2M5LWMzZTY4MzY3ZDcyNCIsImMiOjh9")
            main_page.enter_originalauthor("Test_PowerBI")
            main_page.enter_description("Test_PowerBI")
            main_page.enter_tags("Test_PowerBI")
            main_page.select_whocanseepostonlyme()
            main_page.enter_license("Test_PowerBI")
            main_page.enter_uploadposter()
            main_page.submitpost()
            main_page.check_post_created()

            sleep(5)
        # def test_valid_createpost_powerbi_everybody(self):
        #     self.driver.get("https://sharedataset.com/account/login")
        #     login = Login(driver=self.driver)
        #     login.enter_username("samane_mss@yahoo.com")
        #     login.enter_password("123456S@vdash")
        #     login.click_on_continue_button()
        #     main_page = CreatePost(driver=self.driver)
        #     main_page.check_main_page()
        #     main_page.enter_title("Test_PowerBI_EveryBody")
        #     main_page.select_source_powerbi()
        #     main_page.enter_publicurl(
        #         "https://app.powerbi.com/view?r=eyJrIjoiZDIxOTgwOGQtNmNlOS00NTJmLWE2NWUtYzU4ZWNkOWI0MTFjIiwidCI6IjkyNWJkNTViLTA1MjEtNDAwMy1iN2M5LWMzZTY4MzY3ZDcyNCIsImMiOjh9")
        #     main_page.enter_originalauthor("Test_PowerBI")
        #     main_page.enter_description("Test_PowerBI")
        #     main_page.enter_tags("Test_PowerBI")
        #     main_page.select_whocanseeposteverybody()
        #     main_page.enter_license("Test_PowerBI")
        #     main_page.enter_uploadposter()
        #     main_page.submitpost()
        #     main_page.check_post_created()
        #
        #     sleep(5)

    # def test_valid_createpost_tableau_onlyme(self):
    #     self.driver.get("https://sharedataset.com/posts/create")
    #     login = Login(driver=self.driver)
    #     login.enter_username("samane_mss@yahoo.com")
    #     login.enter_password("123456S@vdash")
    #     login.click_on_continue_button()
    #     main_page = CreatePost(driver=self.driver)
    #     main_page.check_main_page()
    #     main_page.enter_title("Test_Tableau_OnlyMe")
    #     main_page.select_source_tableau()
    #     main_page.enter_publicurl(
    #         "https://public.tableau.com/views/USFruitConsumption/Fruit?:language=en-US&:display_count=n&:origin=viz_share_link")
    #     main_page.enter_originalauthor("Test_OnlyMe")
    #     main_page.enter_description("Test_OnlyMe")
    #     main_page.enter_tags("Test")
    #     main_page.select_whocanseepostonlyme()
    #     main_page.enter_license("Test_OnlyMe")
    #     main_page.enter_uploadposter()
    #     main_page.submitpost()
    #     main_page.check_post_created()
    #
    #     sleep(5)
    #
    # def test_valid_createpost_tableau_everybody(self):
    #     self.driver.get("https://sharedataset.com/account/login")
    #     login = Login(driver=self.driver)
    #     login.enter_username("samane_mss@yahoo.com")
    #     login.enter_password("123456S@vdash")
    #     login.click_on_continue_button()
    #     main_page = CreatePost(driver=self.driver)
    #     main_page.check_main_page()
    #     main_page.enter_title("Test_tableau_EveryBody")
    #     main_page.select_source_tableau()
    #     main_page.enter_publicurl(
    #         "https://public.tableau.com/views/USFruitConsumption/Fruit?:language=en-US&:display_count=n&:origin=viz_share_link")
    #     main_page.enter_originalauthor("Test_EveryBody")
    #     main_page.enter_description("Test_EveryBody")
    #     main_page.enter_tags("Test_EveryBody")
    #     main_page.select_whocanseeposteverybody()
    #     main_page.enter_license("Test_EveryBody")
    #     main_page.enter_uploadposter()
    #     main_page.submitpost()
    #     main_page.check_post_created()
    #     self.driver.refresh(driver=self.driver)
    #
    #     sleep(5)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()
        cls.driver.quit()


sleep(10)
