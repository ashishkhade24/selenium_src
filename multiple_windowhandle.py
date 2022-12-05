from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as Chromeservice

from selenium.webdriver.common.by import By
import time

class Window_handle():
    def demo_window(self):
        driver = webdriver.Chrome(service=Chromeservice(ChromeDriverManager().install()))
        driver.get("https://www.yatra.com/")
        driver.maximize_window()
        time.sleep(3)
        parent_handle= driver.current_window_handle
        print(parent_handle)
        time.sleep(3)
        driver.find_element(By.XPATH,"//a[@title='Citi Emi Offers']//img[@class='conta iner large-banner']").click()
        all_handles=driver.window_handles
        print(all_handles)
        time.sleep(3)
        for handle in all_handles:
            if handle!=parent_handle:
                driver.switch_to.window(handle)
                driver.find_element(By.XPATH,"//i[@class='sprite-footer ico-tgFooter_family']").click()
                time.sleep(3)
                driver.close()
                time.sleep(3)
                break


object=Window_handle()
object.demo_window()


