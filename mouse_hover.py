import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains

class Demo_mousehover():
    def mousehover(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://www.yatra.com/")
        driver.maximize_window()
        actions=ActionChains(driver)
        element=driver.find_element(By.XPATH,"//span[@class='more-arr']")
        actions.move_to_element(element).perform()
        time.sleep(3)
        element1=driver.find_element(By.XPATH,"//span[normalize-space()='Xplore']").click()
        time.sleep(3)

object=Demo_mousehover()
object.mousehover()