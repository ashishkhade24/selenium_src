import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

class Demo_fluent_wait():
    def demo_check(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://login.salesforce.com/?locale=in")
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.find_element(By.ID,"username").send_keys("Ashish khade")
        driver.find_element(By.ID,"password").send_keys("Ashish123")


object = Demo_fluent_wait()
object.demo_check()
