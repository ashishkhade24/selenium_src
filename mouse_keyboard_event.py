from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromiumService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType

driver = webdriver.Chrome(service=ChromiumService(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()))

# driver.get("http://demo.guru99.com/test/newtours/")
# actions=ActionChains(driver)
# home_link=driver.find_element(By.LINK_TEXT,"Home")
# actions.move_to_element(home_link).perform()
# actions.click(home_link).perform()

driver.get("https://www.facebook.com")
actions = ActionChains(driver)
# actions.move_to_element(txtUsername).click(txtUsername).key_down(Keys.SHIFT, txtUsername).send_keys("hello").key_up(Keys.SHIFT, txtUsername).double_click(txtUsername).context_click(txtUsername).perform()
Email=driver.find_element(By.NAME,"email")
actions.move_to_element(Email)
actions.click(Email)
actions.key_down(Keys.SHIFT,Email)
actions.send_keys("hello")
actions.key_up(Keys.SHIFT,Email)
actions.double_click(Email)
actions.perform()
driver.quit()
