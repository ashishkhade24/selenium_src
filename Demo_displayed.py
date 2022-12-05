import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://www.w3schools.com/howto/howto_js_toggle_hide_show.asp")
driver.maximize_window()
element=driver.find_element(By.XPATH,"//div[@id='myDIV']").is_displayed()
time.sleep(3)
print(element)
button=driver.find_element(By.XPATH,"(//button[normalize-space()='Toggle Hide and Show'])[1]").click()
element1=driver.find_element(By.XPATH,"//div[@id='myDIV']").is_displayed()
time.sleep(3)
print(element1)


# driver.get("https://www.yatra.com/hotels")
# driver.maximize_window()
# time.sleep(3)
# ele=driver.find_element(By.XPATH,"//span[@class='txt-ellipses hotel_passengerBox travellerPaxBox']").click()
# time.sleep(3)
# ele1=driver.find_element(By.XPATH,"//body[1]/div[2]/div[1]/section[1]/div[1]/div[1]/div[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[2]/div[3]/div[1]/div[1]/span[2]").click()
# time.sleep(3)
# ele2=driver.find_element(By.TAG_NAME,"select").is_displayed()
# print(ele2)
# time.sleep(3)
# ele3=driver.find_element(By.XPATH,"//span[@class='ddSpinnerMinus disabled']").is_displayed()
# print(ele3)
# time.sleep(3)


