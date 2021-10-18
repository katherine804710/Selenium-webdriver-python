
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
driver = webdriver.Firefox(executable_path = '/Users/family/Downloads/geckodriver')
driver.implicitly_wait (15)
driver.get("http://www.google.com")
#fLoctor = "input[name=q]"
try:
	searchField=WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,"input[name=q]")))
finally:
	driver.quit()
