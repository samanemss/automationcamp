from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
# driver = webdriver.chrome(executable_path="D:\Programs\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())


driver.get("https://sharedataset.com/")

driver.switch_to.new_window('window')
driver.get('http://yahoo.com')
yahoo_window = driver.current_window_handle
print('yahoo handle' + str(yahoo_window))
all_handle = driver.window_handles
print('all_handles' + str(all_handle))
driver.switch_to.window(all_handle[0])

sleep(3)

driver.set_window_position(400,500)
driver.minimize_window()
driver.maximize_window()
driver.fullscreen_window()
