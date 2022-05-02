from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.alert import Alert

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.implicitly_wait(5)
alert = Alert(driver)

driver.get("https://the-internet.herokuapp.com/javascript_alerts")
# driver.find_element(By.XPATH, "//button[text()= 'Click for JS Alert']").click()
# print(alert.text)
# sleep(20)

# driver.find_element(By.XPATH, "//button[text() = 'Click for JS Confirm']").click()
# alert.accept()
# driver.find_element(By.XPATH, "//*[text() = 'You clicked: Ok']")
dom = driver.page_source
# assert 'You clicked: Ok' in dom
# sleep(20)

driver.find_element(By.XPATH, "//button[text() = 'Click for JS Prompt']").click()
sleep(10)
alert.send_keys("This is AutomationCamp")
alert.accept()
assert "This is AutomationCamp" in driver.page_source
sleep(10)