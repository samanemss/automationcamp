from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
actions = ActionChains(driver)
driver.maximize_window()
driver.get("http://google.com")
driver.implicitly_wait(3)
search_box = driver.find_element('name', 'q')
# search_box.send_keys("Selenium")
# search_box.send_keys('Selenium' + Keys.ENTER)

sleep(20)
