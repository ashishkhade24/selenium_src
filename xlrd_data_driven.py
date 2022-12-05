import xlrd
import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as Chromeservice
driver=webdriver.Chrome(service=Chromeservice(ChromeDriverManager().install()))

file_location = "../test_data/xlrd_data_driven_data.xls"

result_data = []

driver.get("https://the-internet.herokuapp.com/login")

with xlrd.open_workbook(filename=file_location) as my_work_book:
    my_sheet = my_work_book.sheet_by_index(0)
    no_of_columns = my_sheet.ncols
    no_of_rows = my_sheet.nrows
    for row_index in range(no_of_rows):
        username = my_sheet.cell_value(row_index, 0)
        password = my_sheet.cell_value(row_index, 1)
        result_data.append([username, password, "PASSED"])

        driver.find_element(By.ID, "username").clear()
        driver.find_element(By.ID, "username").send_keys(username)
        driver.find_element(By.ID, "password").clear()
        driver.find_element(By.ID, "password").send_keys(password)
        time.sleep(2)
driver.quit()
print("RESULT DATA = ", result_data)

