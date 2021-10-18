
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import unittest
import time
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.common.keys import Keys



class SelectProduct(unittest.TestCase):
	def setUp(self):
		global driver
		driver = webdriver.Firefox(executable_path = '/Users/family/Downloads/geckodriver')
		driver.implicitly_wait (15)
		driver.get("https://travelingtony.weebly.com/store/p1/Leatherback_Turtle_Picture.html")

	def test_Select(self):
		# searchField = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_name('q'))
		# searchField.send_keys("leatherback")
	

		# searchButtonElement = WebDriverWait(driver,10).until(lambda driver:driver.find_element_by_css_selector('span.wsite-search-button'))
		# searchButtonElement.click()
		
		# searchProduct = WebDriverWait(driver,15).until(lambda driver:driver.find_element_by_css_selector('span.wsite-search-product-name'))
		# searchProduct.click()
		# quantityDropDown = WebDriverWait(driver,10).until(lambda driver:driver.find_element_by_id ('wsite-com-product-option-Quantity'))
		# Select(quantityDropDown).select_by_visible_text("2")

		menu=driver.find_element_by_xpath('//*[@id="wsite-com-product-option-Quantity"]')
		ActionChains(driver).move_to_element(menu).click()
		ActionChains(driver).send_keys(Keys.ENTER).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).perform()
		driver.implicitly_wait (15)




	def tearDown(self):
		driver.quit()

if __name__ == "__main__":
   unittest.main()
