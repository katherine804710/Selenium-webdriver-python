from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

'''
test case: enter"sa" in search text field, then select "san francisco" from auto suggestion list, then verify "we've
your easy ride accross town,"
'''

driver=webdriver.Firefox(executable_path = '/Users/mzhou/OneDrive/Desktop/geckodriver')
driver.get("https://www.lyft.com/rider/cities/")

searchTextField=driver.find_element_by_name('search-cities') #by classname,name,ID,xpath, css selector
searchTextField.send_keys("sa")
firstList= WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID,"react-autowhatever-1--item-0")))
firstList.click()
driver.quit()
              
