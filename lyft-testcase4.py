from selenium import webdriver
import requests
'''
test case:
1.find all the city links and check none of the links are throwing 'page not found' error.Another way to test
is to fetch all the links and compare with the right lists. 
2.locate text filed and enter city names then click search button. Ask developers for full city list.
verify the map in search result page includes the city or verify the string: We’ve got your easy ride across town,
3.change country to Canada, and verify all the Canada city links are working properly.
'''
#open lyft cities link in firefox
driver=webdriver.Firefox(executable_path = '/Users/family/Downloads/geckodriver')
driver.implicitly_wait(15)
driver.get("https://www.lyft.com/rider/cities/")

cityLinks=driver.find_elements_by_class_name('_1dax37')
count=0
extracLinks=[]
for link in cityLinks:
    extracLinks.append(link.get_attribute('href'))
    statusCode=requests.head(link.get_attribute('href')).status_code
    # print(link.get_attribute('href'))
    # print(statusCode)
    count+=1
    if statusCode>=400:# 400 Bad Request, 404 Not Found, 401 Unauthorized
        print(link + "is broken")
print(count)

driver.quit()


