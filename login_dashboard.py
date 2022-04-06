from selenium import webdriver

import time

from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:\webdriver\chromedriver.exe")
driver.maximize_window()
driver.get("https://admin0-trials7401.orangehrmlive.com/")
driver.find_element(By.ID,"txtUsername").send_keys("Admin")
driver.find_element(By.ID,"txtPassword").send_keys("DWj2q2PUv@")
driver.find_element(By.CLASS_NAME,"button-holder").click()
act_title=driver.title
exp_title="Dashboard"
if act_title == exp_title:
    print("Login test passed")
else:
    print("Login test failed")
driver.close();