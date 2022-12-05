from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as Chromeservice

from selenium.webdriver.common.by import By
import time

class Iframe_handle():
    def demo_iframe(self):
        driver = webdriver.Chrome(service=Chromeservice(ChromeDriverManager().install()))
        driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_iframe_frameborder_css")
        driver.maximize_window()
        #find element by frame locator
        #driver.switch_to.frame(driver.find_element(By.XPATH,"//iframe[@id='iframeResult']"))
        #find element by ID
        driver.switch_to.frame(driver.find_element(By.ID, "iframeResult"))
        driver.switch_to.frame(0)
        driver.find_element(By.XPATH,"//a[@id='navbtn_tutorials']").click()
        time.sleep(4)

object=Iframe_handle()
object.demo_iframe()
