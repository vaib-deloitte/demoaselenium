from selenium import webdriver

import time

from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:\webdriver\chromedriver.exe")
driver.maximize_window()
driver.get("https://admin0-trials7401.orangehrmlive.com/")
driver.find_element(By.ID,"txtUsername").send_keys("Admin")
driver.find_element(By.ID,"txtPassword").send_keys("DWj2q2PUv@")
driver.find_element(By.CLASS_NAME,"button-holder").click()
driver.find_element(By.ID,"menu_pim_viewPimModule").click()
time.sleep(3)
driver.find_element(By.XPATH,'//*[@id="menu_pim_addEmployee"]/span[2]').click()
time.sleep(3)
#enter first name
driver.find_element(By.XPATH,"//input[@id='first-name-box']").send_keys("Vaibhav")
# enter middle name
driver.find_element(By.CSS_SELECTOR,"#middle-name-box").send_keys("   ")
# enter last name
driver.find_element(By.XPATH,'//*[@id="last-name-box"]').send_keys("Krishana")
# enter employee id
driver.find_element(By.ID,"employeeId").send_keys(9472)

driver.find_element(By.CSS_SELECTOR,"#modal-holder > div > div > div > div.modal-body > form > oxd-decorator > div > div.form-group.col-8 > div > div:nth-child(2) > div > div.form-group.col-5.remove-right-padding > div > div.dropdown.bootstrap-select.select-dropdown > button").click()
time.sleep(3)
#location
driver.find_element(By.XPATH,"//*[@id='bs-select-1-7']").click()
#next button
driver.find_element(By.XPATH,'//*[@id="modal-save-button"]').click()