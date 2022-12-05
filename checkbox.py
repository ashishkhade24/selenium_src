import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select

class Checkbox_demo():
    def demo_check(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://www.sugarcrm.com/au/request-demo/")
        time.sleep(3)
        driver.maximize_window()
        ch1=driver.find_element(By.ID,"interest_market_c0").click()
        time.sleep(3)

obj=Checkbox_demo()
obj.demo_check()
