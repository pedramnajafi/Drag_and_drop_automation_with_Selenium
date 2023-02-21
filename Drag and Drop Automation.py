from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('http://dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html')
time.sleep(1)
source = driver.find_element(By.XPATH,'//*[@id="box3"]')
dest = driver.find_element(By.XPATH,'//*[@id="box103"]')
time.sleep(5)

actions = ActionChains(driver)
actions.drag_and_drop(source, dest).perform()

time.sleep(100)