import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains

class Demo_dragdrop():
    def demo_check(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://jqueryui.com/droppable/")
        driver.maximize_window()
        driver.switch_to.frame(driver.find_element(By.XPATH,"//iframe[@class='demo-frame']"))
        ele1=driver.find_element(By.ID,"draggable")
        ele2=driver.find_element(By.ID,"droppable")
        actions=ActionChains(driver)
        actions.drag_and_drop(ele1,ele2).perform()
        #actions.drag_and_drop_by_offset(ele1,80,40).perform()
        time.sleep(4)

object = Demo_dragdrop()
object.demo_check()
