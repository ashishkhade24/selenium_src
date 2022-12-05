from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as Chromeservice
driver=webdriver.Chrome(service=Chromeservice(ChromeDriverManager().install()))
from selenium.webdriver.common.by import By
import time
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)
driver = webdriver.Chrome(chrome_options=chrome_options)
driver = webdriver.Chrome(executable_path=r'D:\Python_Pr\chromedriver.exe')
class Demo_screenshot():
    def check(self):
        driver = webdriver.Chrome(service=Chromeservice(ChromeDriverManager().install()))
        driver.get("https://secure.yatra.com/social/common/yatra/register")
        continue_demo=driver.find_element(By.XPATH,"//button[@id='login-continue-btn']")
        time.sleep(3)
        continue_demo.screenshot(".//tests.png")
        time.sleep(3)
        continue_demo.click()
        driver.get_screenshot_as_file("D:\\screenshot\\test01.png")
        driver.save_screenshot(".//test02.png")

object=Demo_screenshot()
object.check()

