
from selenium import webdriver
import requests
driver=webdriver.Firefox(executable_path = '/Users/family/Downloads/geckodriver')
driver.get("https://www.lyft.com/rider/cities/")
countryButton=driver.find_element_by_css_selector('._3gzABI')
countryButton.click()
canada=driver.find_element_by_css_selector('li._2stBGc:nth-child(3)')
canada.click()
caCities=driver.find_elements_by_class_name('_1dax37')
# extracLinks=[]
for link in caCities:
    # link.click()
    # extracLinks.append(link.get_attribute('href'))
    statusCode=requests.head(link.get_attribute('href')).status_code
    # print(link.get_attribute('href'))
    # print(statusCode)
    if statusCode>=400:
        print(link + "is broken")
driver.quit()
