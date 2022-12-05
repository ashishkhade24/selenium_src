from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
import time

class Java_script():
    def Demo_js(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.execute_script("window.open('https://www.yatra.com/')")
        driver.maximize_window()
        time.sleep(4)
        demo_element=driver.execute_script("return document.getElementsByTagName('p')[1];")
        driver.execute_script("arguments[1].click();",demo_element)


object=Java_script()
object.Demo_js()


