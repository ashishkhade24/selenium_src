import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromiumService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.options import ChromiumOptions
driver = webdriver.Chrome(service=ChromiumService(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()))

driver.get("http://demo.guru99.com/test/delete_customer.php")
driver.maximize_window()
driver.find_element(By.NAME,"cusid").send_keys("12345")
time.sleep(3)
driver.find_element(By.NAME,"submit").submit()
time.sleep(3)

alert=driver.switch_to.alert

alert_msg=alert.text

print("alert_text=",alert_msg)
alert.accept()
driver.quit()

