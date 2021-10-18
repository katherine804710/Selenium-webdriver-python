from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import unittest
class TestSearch(unittest.TestCase):
    def setUp(self):
        global driver
        driver=webdriver.Firefox(executable_path= '/Users/family/Downloads/geckodriver')
        driver.get('https://www.lyft.com/rider/cities/')

    def testSearch(self):
        searchField=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.NAME,"search-cities")))
        searchField.send_keys("sa")
        firstList=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID,"react-autowhatever-1--item-0")))
        firstList.click()
        actualMessage=WebDriverWait(driver,10).\
            until(EC.presence_of_element_located((By.CSS_SELECTOR,"h1.StyledText-cx1xxi-0")))
        expectedMessage='We’ve got your easy ride across town, San Francisco.'
        self.assertEqual(actualMessage.text,expectedMessage)

        mainPage = driver.current_window_handle
        for handle in driver.window_handles:
            if handle != mainPage:
                driver.switch_to.window(handle)
                break
        phoneNo = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "phone")))
        phoneNo.send_keys('9319330101')
        signUp = driver.find_element_by_xpath("//span[text()='SIGN UP']")
        signUp.click()
        linkMessage = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CSS_SELECTOR,'.bdRPuj')))
        self.assertEqual(linkMessage.text, "We have sent a link to 9319330101.")

    def tearDown(self):
        driver.quit()
if __name__=="__main__":
    unittest.main()
