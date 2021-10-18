
from selenium import webdriver
driver = webdriver.Firefox(executable_path = '/Users/family/Downloads/geckodriver')
driver.implicitly_wait (15)
driver.get("http://www.google.com")
searchField = driver.find_element_by_css_selector ("input[name=a")
driver.quit()
