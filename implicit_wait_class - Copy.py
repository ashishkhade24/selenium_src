from selenium.webdriver.common.by import By
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as Chromeservice
driver=webdriver.Chrome(service=Chromeservice(ChromeDriverManager().install()))
driver.implicitly_wait(10)
driver.get("https://www.facebook.com/" )
driver.find_element(By.NAME,"websumit").click()

driver.quit()