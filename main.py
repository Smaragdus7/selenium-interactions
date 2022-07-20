from selenium import webdriver
from selenium.webdriver.common.by import By

# S E T T I N G    W E B D R I V E R
chrome_driver_path = r"C:\Users\GC-SI\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

# S C R A P I N G    P Y T H O N . O R G
driver.get("https://www.python.org/")
events_times = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
times = [time.text for time in events_times]

events_names = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")
names = [name.text for name in events_names]

events_dictionary = {}
for n in range(len(times)):
    events_dictionary[n] = {
        "time": times[n],
        "name": names[n],
    }

print(events_dictionary)

# driver.close()
driver.quit()
