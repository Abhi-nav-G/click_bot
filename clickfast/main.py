from selenium import webdriver
from selenium.webdriver.common.keys import Keys

PATH = 'C:\\Program Files (x86)\\chromedriver.exe'
driver = webdriver.Chrome(PATH)


driver.get('https://clickspeedtest.com')
driver.set_window_size(1024, 600)
driver.maximize_window()
button = driver.find_element_by_id('clicker')

for i in range(1000):
    button.click()
    