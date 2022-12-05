import time
from selenium.webdriver.common.by import By

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromiumService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType

driver = webdriver.Chrome(service=ChromiumService(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()))

driver.get("http://www.seleniumframework.com/demo-sites/")

driver.refresh()

time.sleep(2)

driver.find_element(By.XPATH, value="//a[@href='http://www.seleniumframework.com/introduction/']").click()

time.sleep(2)

driver.find_element(By.LINK_TEXT, value="PYTHON").click()

time.sleep(2)

driver.back()

time.sleep(2)

driver.forward()

time.sleep(2)

driver.quit()


