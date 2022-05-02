from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
import os
from pathlib import Path
from selenium.webdriver.chrome.options import Options

chrome_options = Options
chrome_options.add_argument("--incognito")
# driver = webdriver.chrome(executable_path="D:\Programs\chromedriver_win32\chromedriver.exe")
# driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install()),chrome_options=chrome_options

driver.get("http://yahoo.com")
sleep(3)
#driver.find_element('id', 'ybar-sbq')

driver.execute_script("window.scrollTo(0, document.body.scrollheight);")
sleep(2)

current_path = Path(__file__).parent
file_name = os.path.join(str(current_path), 'session2.png')
driver.save_screenshot(file_name)