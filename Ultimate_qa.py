import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as Chromeservice
driver=webdriver.Chrome(service=Chromeservice(ChromeDriverManager().install()))
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
class Ultimate_qa():
    def basic(self):

        driver.get("https://ultimateqa.com/complicated-page")
        driver.maximize_window()
        time.sleep(3)
        driver.find_element(By.XPATH,"//ul[@id='menu-home-page-menu']//a[normalize-space()='Automation Exercises']").click()
        time.sleep(3)
        driver.find_element(By.XPATH,"//a[normalize-space()='Interactions with simple elements']").click()
        time.sleep(3)

    def basic1(self):

        #obj.basic()

        button1= driver.find_element(By.ID,"idExample").click()
        time.sleep(3)
        driver.back()
        button2= driver.find_element(By.CLASS_NAME,"buttonClass").click()
        time.sleep(3)
        driver.back()
        button3= driver.find_element(By.NAME,"button1").click()
        time.sleep(3)
        driver.back()
        # link= driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/article[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]").click()
        # time.sleep(3)
        # driver.back()
        driver.close()


    def basic2(self):
        #obj.basic1()

        driver.find_element(By.XPATH,"//a[normalize-space()='Click Me']").click()
        time.sleep(2)
        driver.back()
        driver.find_element(By.XPATH,"//a[normalize-space()='Go to login page']").click()
        time.sleep(2)
        driver.find_element(By.ID,"user[email]").send_keys("testashish@mailinator.com")
        time.sleep(2)
        driver.find_element(By.ID,"user[password]").send_keys("Ashish@1105")
        time.sleep(2)
        driver.find_element(By.ID,"user[remember_me]").click()
        time.sleep(2)
        driver.find_element(By.XPATH,"//input[@value='Sign in']").click()
        time.sleep(2)
        driver.back()
        driver.close()

    def check(self):
        obj.basic()
        driver.find_element(By.ID,"simpleElementsLink").click()
        driver.back()
        driver.find_element(By.ID,"et_pb_contact_name_0").send_keys("Ashu")
        driver.find_element(By.XPATH,"//input[@id='et_pb_contact_email_0']").send_keys("testashish@mailinator.com")
        driver.find_element(By.XPATH,"//button[normalize-space()='Email Me!']").click()
        time.sleep(2)
        radio_buttons=driver.find_elements(By.XPATH,"//div[7]//div[1]//div[1]//div[1]//form//input")
        for radio_Buttons in radio_buttons:
            count=0
            radio_Buttons.click()
            time.sleep(3)
            if count==3:
                break

        option1=driver.find_element(By.XPATH,"//input[@value='Bike']").click()
        time.sleep(3)
        option2=driver.find_element(By.XPATH,"//input[@value='Car']").click()
        time.sleep(3)

        drop_down=Select(driver.find_element(By.XPATH,"//div[contains(@class,'et_pb_blurb_description')]//select"))
        time.sleep(3)
        drop_down.select_by_index(1)
        time.sleep(2)
        drop_down.select_by_index(2)
        time.sleep(2)
        driver.close()

obj=Ultimate_qa()
obj.check()












