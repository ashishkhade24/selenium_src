import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select

options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications": 2}
options.add_experimental_option("prefs", prefs)
# driver = webdriver.Chrome(chrome_options=chrome_options)
driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

class Login():
    def check(self):
        driver.get("https://dev.itshandsdown.com/login")
        driver.maximize_window()
        driver.find_element(By.NAME, "email").send_keys("testashish@mailinator.com")
        time.sleep(1)
        driver.find_element(By.NAME, "password").send_keys("Ashish@1105")
        time.sleep(1)
        driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
        time.sleep(1)

    def check1(self):
        obj.check()

        wait = WebDriverWait(driver, 10)
        buttons = wait.until(EC.visibility_of_all_elements_located((By.XPATH, "//div[contains(@class,'CategoryBar')]")))
        for button in buttons:
            button.click()
            print("button_name" + button.text + "successful")
            time.sleep(3)
        # for button in driver.find_elements(By.XPATH, "//div[contains(@class,'CategoryBar')]"):
        #     button.click()
        #     print("button_name" + button.text + "successful")
        #     time.sleep(1)

    # obj.check1()

    def check2(self):
        obj.check()

        driver.find_element(By.XPATH,
                            "/html[1]/body[1]/div[1]/div[1]/div[3]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]").click()
        time.sleep(2)
        img = driver.find_elements(By.TAG_NAME, "img")
        time.sleep(3)
        print(len(img))
        time.sleep(3)
        driver.close()
        driver.quit()

    def check3(self):
        obj.check()
        driver.find_element(By.XPATH, "//div[@href='/my-profile?tab=list']").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//button[normalize-space()='Edit Profile']").click()
        time.sleep(2)
        actions = ActionChains(driver)
        web = driver.find_element(By.ID, "last_name")
        time.sleep(2)
        actions.double_click(web).send_keys(Keys.BACKSPACE).send_keys("Khade").perform()
        driver.find_element(By.NAME, "bio_description").send_keys("Software tester")
        time.sleep(2)
        driver.find_element(By.XPATH, "//button[normalize-space()='Save Edits']").click()
        time.sleep(2)
        driver.close()
        driver.quit()

    def check4(self):
        obj.check()

        # drop_down=Select(driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[2]/div[2]/*[name()='svg'][1]"))
        # time.sleep(2)
        # drop_down.select_by_index(0)
        # time.sleep(2)
        # driver.back()
        # driver.refresh()
        # time.sleep(2)`

        # driver.find_element(By.XPATH,"//*[@id='__next']/div/div[4]/svg/path[2]").click()

obj = Login()
#obj.check1()
#obj.check2()
#obj.check3()
#obj.check4()


