from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
import time

class Handsdown():
    def check(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://dev.itshandsdown.com/login")
        driver.maximize_window()
        time.sleep(3)
        User_name=driver.find_element(By.NAME,"email")
        User_name.click()
        User_name.send_keys("testashish@mailinator.com")
        pass_word=driver.find_element(By.NAME,"password")
        pass_word.click()
        pass_word.send_keys("Ashish@1105")
        driver.find_element(By.XPATH,"//div[4]").click()
        time.sleep(3)

        boook=driver.find_element(By.XPATH,"//p[normalize-space()='Books']").click()
        time.sleep(3)
        feed=driver.find_element(By.XPATH,"//div[@class='feed__CenterContainer-sc-1wvitii-3 dlDkDL']").is_displayed()
        driver.save_screenshot(".//test04.png")
        time.sleep(3)
        print(feed)

object=Handsdown()
object.check()



