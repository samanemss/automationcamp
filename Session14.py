from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert

service = Service(executable_path=ChromeDriverManager().install())

options = webdriver.ChromeOptions()
user_dir = "D:/Projects/automationcamp/user_dir"
options.add_argument(f"user-data-dir={user_dir}")
driver = webdriver.Chrome(service=service, options=options)
driver.maximize_window()
driver.implicitly_wait(3)

driver.get("https://app.clockify.me/en/signup")
windows = driver.window_handles
driver.switch_to.window([0])
driver.find_element(By.XPATH, "//*input[@type= 'email']").send_keys("kahkdgakg@pp.com")
driver.find_element(By.XPATH, "//*input[@type= 'password']").send_keys("123456")
driver.find_element(By.XPATH, "//*button[@type= 'submit']").click()

for i in range(10):
    try:
        driver.find_element(By.id, "sidebar-menu")
        break
    except:
        sleep(10)

sleep(10)
options.add_argument("--incognito")