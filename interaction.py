from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# S E T T I N G    W E B D R I V E R
chrome_driver_path = r"C:\Users\GC-SI\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

# I N T E R A C T I N G    W I T H    W i k i p e d i a
driver.get("https://en.wikipedia.org/wiki/Main_Page")
num = driver.find_element(By.XPATH, '//*[@id="articlecount"]/a[1]')
num.click()

search_bar = driver.find_element(By.NAME, "search")
search_bar.send_keys("Python")
search_bar.send_keys(Keys.ENTER)

