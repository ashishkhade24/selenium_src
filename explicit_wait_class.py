from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as Chromeservice
driver=webdriver.Chrome(service=Chromeservice(ChromeDriverManager().install()))
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver.get("https://www.facebook.com/" )

try:
    element = WebDriverWait(driver, 10,2).until(
        EC.visibility_of_element_located((By.NAME, "websubmit")))
    element.click()
except Exception:
    pass

driver.quit()
