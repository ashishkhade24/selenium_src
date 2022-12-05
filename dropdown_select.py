from selenium.webdriver.support.ui import Select
import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromiumService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType

driver = webdriver.Chrome(service=ChromiumService(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()))

# driver.get("http://demo.guru99.com/test/newtours/register.php")
# driver.maximize_window()
#
# drpCountry =Select(driver.find_element(By.NAME,"country"))
# time.sleep(2)
# drpCountry.select_by_visible_text("ANTARCTICA")
# time.sleep(2)
# drpCountry.select_by_index(4)
# time.sleep(3)
# driver.close()
# driver.quit()

driver.get("http://jsbin.com/osebed/2")
driver.maximize_window()

fruits=Select(driver.find_element(By.ID,"fruits"))
assert fruits.is_multiple
fruits.select_by_visible_text("Banana")
fruits.select_by_visible_text("Apple")
time.sleep(3)
fruits.deselect_by_visible_text("Banana")
time.sleep(3)
fruits.deselect_by_visible_text("Apple")
time.sleep(3)
fruits.select_by_index(2)
time.sleep(3)
driver.quit()



