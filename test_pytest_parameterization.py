import pytest
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as Chromeservice
driver=webdriver.Chrome(service=Chromeservice(ChromeDriverManager().install()))
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

test_data = [["user1", "pass1"],
             ["user2", "pass2"],
              ["user3", "pass3"],
              ["user4", "pass4"],
              ["user5", "pass5"],
              ["user6", "pass6"],
             ]

@pytest.mark.parametrize("username, password", test_data)
def test_login(username, password):
    driver = webdriver.Chrome(service=Chromeservice(ChromeDriverManager().install()))
    driver.get("https://the-internet.herokuapp.com/login")
    driver.find_element(By.ID, "username").clear()
    driver.find_element(By.ID, "username").send_keys(username)
    driver.find_element(By.ID, "password").clear()
    driver.find_element(By.ID, "password").send_keys(password)

    # If username and password are correct
    # user lands on homepage
    time.sleep(3)
    driver.quit()

# test_filename.py
# filename_test.py

# ABC.py

# src/test_filename.py
# src/filename_test.py
# src/ABC.py

# pytest ABC.py

