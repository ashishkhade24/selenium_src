import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains

class Demo_slider():
    def check(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get(("https://bit.ly/3Sj7U6p"))
        driver.maximize_window()
        time.sleep(3)
        ele1=driver.find_element(By.XPATH,"//a[contains(@class,'left-handle')]")
        ele2 = driver.find_element(By.XPATH, "//a[contains(@class,'right-handle')]")
        actions=ActionChains(driver)
        actions.drag_and_drop_by_offset(ele1,60,0).perform()
        time.sleep(3)
        # actions.click_and_hold(ele1).pause(1).move_by_offset(50,0).release().perform()
        # actions.move_to_element(ele1).click_and_hold(ele1).move_by_offset(80,0).release().perform()
        actions.drag_and_drop_by_offset(ele2, -50, 0).perform()
        time.sleep(3)
        driver.close()
        driver.quit()


obj=Demo_slider()
obj.check()
