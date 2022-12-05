import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select



class Drop_down_demo():
    def demo_dropdown(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://www.salesforce.com/in/form/signup/freetrial-sales/?d=topnav2-btn-ft")
        driver.maximize_window()
        drop_down = driver.find_element(By.NAME, "UserTitle")
        dd = Select(drop_down)
        dd.select_by_index(1)
        time.sleep(3)
        # dd.select_by_visible_text(" Marketing / PR Manager")
        # time.sleep(3)
        dd.select_by_value("Customer_Service_Manager_AP")
        time.sleep(3)

obj=Drop_down_demo()
obj.demo_dropdown()
