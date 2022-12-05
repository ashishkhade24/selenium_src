from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
import  time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Demo_explicit_wait():
    def check(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://www.yatra.com/")
        time.sleep(3)
        driver.maximize_window()
        depart_from= driver.find_element(By.XPATH,"//input[@id='BE_flight_origin_city']")
        time.sleep(3)
        depart_from.click()
        time.sleep(3)
        depart_from.send_keys("New Delhi")
        time.sleep(3)
        depart_from.send_keys(Keys.ENTER)
        time.sleep(3)
        going_to=driver.find_element(By.XPATH,"//input[@id='BE_flight_arrival_city']")
        time.sleep(3)
        going_to.click()
        time.sleep(3)
        going_to.send_keys("New")
        time.sleep(3)
        search_result=driver.find_elements(By.XPATH,"//div[@class='viewport']//div[1]/li")
        print(len(search_result))
        for results in search_result:
            if "New York (JFK)" in results.text:
                results.click()
                time.sleep(3)
                break

        wait=WebDriverWait(driver,10)
        wait.until(EC.element_to_be_clickable((By.XPATH,"//input[@id='BE_flight_origin_date']"))).click
        # start_date=driver.find_element(By.XPATH,"//input[@id='BE_flight_origin_date']")
        # start_date.click()
        # date=driver.find_element(By.XPATH,"(//td[@id='02/10/2022'])[1]")
        # date.click()
        all_dates=wait.until(EC.element_to_be_clickable((By.XPATH,"//div[@id='monthWrapper']//tbody//td[@class!='inActiveTD']")))
        #all_dates=driver.find_elements(By.XPATH,"//div[@id='monthWrapper']//tbody//td[@class!='inActiveTD']")
        for date in all_dates:
            if date.get_attribute("data-date") == "15/10/2022":

                date.click()
                print(date)

                break

auto=Demo_explicit_wait()
auto.check()



