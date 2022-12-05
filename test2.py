from selenium.webdriver.common.by import By
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromiumService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType

driver = webdriver.Chrome(service=ChromiumService(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()))
driver.get("http://demo.guru99.com/test/radio.html")
driver.maximize_window()
radio1=driver.find_element(By.ID,"vfb-7-1")
radio2=driver.find_element(By.ID,"vfb-7-2")
time.sleep(3)

radio1.click()
time.sleep(3)
radio2.click()
time.sleep(3)

option1=driver.find_element(By.ID,"vfb-6-0")
time.sleep(3)
option1.click()

if option1.is_selected():
    print("checkbox is toggled on")
else:
    print("checkbox is toggled off")

driver.close()
driver.quit()
