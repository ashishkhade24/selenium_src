import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as Chromeservice
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(service=Chromeservice(ChromeDriverManager().install()))
driver.get("https://ultimateqa.com/complicated-page")
driver.maximize_window()
# Exe= driver.find_element(By.XPATH,"//ul[@id='menu-home-page-menu']//a[normalize-space()='Automation Exercises']").click()
# time.sleep(2)
# Exe1=driver.find_element(By.XPATH,"//*[@id='post-507']/div/div[1]/div/div[2]/div/div[1]/div/div/div/div/ul/li[1]/a").click()
# time.sleep(2)
# Exe2=driver.find_element(By.XPATH,"//*[@id='post-579']/div/div[1]/div/div/div[3]/div[1]/div[1]/a").click()
# time.sleep(2)
# Exe3=driver.find_element(By.XPATH,"//*[@id='post-579']/div/div[1]/div/div/div[5]/div[1]/ul[1]/li/a").click()
# time.sleep(2)
# driver.back()
# Exe4=driver.find_element(By.XPATH,"//div[@id='et-main-area']//div[contains(@class,'et_pb_css_mix_blend_mode_passthrough et-last-child')]//ul[1]//li[1]//a[1]").click()
# time.sleep(2)
# driver.back()

def action_chain():
    actions=ActionChains(driver)

    name=driver.find_element(By.ID,"et_pb_contact_name_0")
    actions.move_to_element(name)
    actions.click(name)
    actions.send_keys("Ashish")
    actions.double_click(name)
    time.sleep(3)
    email=driver.find_element(By.ID,"et_pb_contact_email_0")
    actions.move_to_element(email)
    actions.click(email)
    actions.send_keys("ashishkhade11@gmail.com")
    time.sleep(3)
    message=driver.find_element(By.ID,"et_pb_contact_message_0")
    actions.move_to_element(message)
    actions.click(message)
    actions.send_keys("Hello User")
    time.sleep(3)
    actions.perform()
    submit=driver.find_element(By.CLASS_NAME,"et_pb_contact_captcha_question").text
    sum=(eval(submit))
    print(sum)
    time.sleep(3)
    captcha=driver.find_element(By.NAME,'et_pb_contact_captcha_0').send_keys(sum)
    time.sleep(3)
    submit_button=driver.find_element(By.NAME,'et_builder_submit_button').click()
    time.sleep(3)

#action_chain()

def element():

    buttons=WebDriverWait(driver,10).until(EC.visibility_of_all_elements_located((By.XPATH,"//div[@class='et_pb_row et_pb_row_2 et_pb_row_4col']//div//div")))
    for button in buttons:
        button.click()
        time.sleep(2)
    # print([element.click() for element in WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located((By.XPATH,"//div[@class='et_pb_row et_pb_row_2 et_pb_row_4col']//div/div")))])
    # button=[element.click() for element in WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located((By.XPATH,"//div[@class='et_pb_row et_pb_row_2 et_pb_row_4col']//div/div")))]
    # print(len(button))
    # print("buttons working fine")

# element()

def social_media():
    # links=WebDriverWait(driver,10).until(EC.visibility_of_all_elements_located((By.XPATH,"//*[@id='post-579']/div/div[1]/div/div/div[5]//div//li")))
    for link in WebDriverWait(driver,10).until(EC.visibility_of_all_elements_located((By.XPATH,"//*[@id='post-579']/div/div[1]/div/div/div[5]//div//li"))):
        # count=0
        link.click()
        driver.back()
        # if count==10:
        time.sleep(3)
        print("Link_name"+ link.text)
    driver.close()
    driver.quit()

social_media()

def hover_over():
    actions=ActionChains(driver)
    driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/header[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/img[1]").click()
    time.sleep(3)
    images=driver.find_elements(By.XPATH,"//*[@id='post-217173']/div/div[1]/div/div[3]/div[2]/div/div")
    time.sleep(2)
    for image in images:

        count=0
        actions.move_to_element(image)
        time.sleep(3)
        if count==4:
            break
    driver.close()
    driver.quit()

#hover_over()
















