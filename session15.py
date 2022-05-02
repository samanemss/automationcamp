from seleniumwire import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import json
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
user_dir = "D:/Projects/automationcamp/user_dir"
options = webdriver.ChromeOptions()
options.add_argument(f"user-data-dir={user_dir}")
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
driver.maximize_window()
driver.implicitly_wait(3)

driver.get("https://wikipedia.com")

def get_all_requests_of_session():
 return driver.requests

def get_specific-get_all_requests_of_session(url, property_return, all_requests=None):

    Return a requests to the 'url1'




