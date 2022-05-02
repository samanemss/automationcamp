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
driver.implicitly_wait(1.5)

# driver.get("https://trytestingthis.netlify.app/")
# sleep(20)
#
# driver.execute_script("window.scrollBy(0,200)")
# sleep(20)
#
# driver.execute_script("window.scrollTo(0,500)")
# sleep(20)

# driver.get("https://www.imdb.com/chart/top")

# element = driver.find_element('link text', 'The Handmaiden')
# print(element)
# driver.execute_script("arguments[0].scrollIntoView();", element)
#
# sleep(1)

# def scroll_to_find_element(locator,pixel):
#     for i in range(10):
#         try:
#           driver.find_element(locator[0], locator[1])
#         return True
#         except:
#             driver.execute_script(f"window.scrollBy(0, {str(pixel)})")
#             sleep(5)
#         return  False
#    result = scroll_to_find_element(['link text', 'aakhkv'],1800)
# print(result)
# driver.execute_script("document.querySelector('table td:last-child').scrollIntoView")
# element = driver.find_element('link text', 'Andrei Rublev')
# print(element)
#
# result = element.is_displayed()





