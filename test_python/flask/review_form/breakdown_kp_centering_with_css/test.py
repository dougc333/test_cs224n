# this will take too long.

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("file:///Users/dc/test_stuff/flask/review_form1/breakdown_kp_centering_with_css/flexbox_method3.html")
element = driver.find_element(By.ID, "container")
print("element:", element)
driver.close()
