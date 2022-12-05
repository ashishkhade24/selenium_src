import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


url=driver.get("http://training.openspan.com/login")
driver.maximize_window()
user_name=driver.find_element(By.ID,"user_name").send_keys("ashish")
time.sleep(3)
user_pass=driver.find_element(By.ID,"user_pass").send_keys("ash123")
time.sleep(3)
button=driver.find_element(By.ID,"login_button").is_enabled()
time.sleep(3)
print(button)
