import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains

class Demo_right_doubleclick():
    def check(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://demo.guru99.com/test/simple_context_menu.html")
        driver.maximize_window()
        time.sleep(3)
        actions=ActionChains(driver)
        element=driver.find_element(By.XPATH,"//span[@class='context-menu-one btn btn-neutral']")
        actions.context_click(element).perform()
        time.sleep(3)
        # copy_ele=driver.find_element(By.XPATH,"//span[normalize-space()='Copy']").click()
        # time.sleep(3)
        # actions = ActionChains(driver)
        # element1=driver.find_element(By.XPATH,"//button[normalize-space()='Double-Click Me To See Alert']")
        # actions.double_click(element1)
        # time.sleep(4)
        # driver.close()
        # driver.quit()

obj=Demo_right_doubleclick()
obj.check()