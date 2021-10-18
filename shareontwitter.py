
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import unittest
import time





class ShareOnPinterest(unittest.TestCase):
	def setUp(self):
		global driver
		driver = webdriver.chrome() #(executable_path = '/Library/Python/2.7/site-packages/selenium/webdriver/firefox/webdriver.py')
		driver.implicitly_wait (15)
		driver.get("http://travelingtony.weebly.com/store/p1/Leatherback_Turtle_Picture.html")

	def test_ShareOnPinterest(self):

		#user=yangzifeihotmail.com
		driver.find_element_by_class_name('wsite-com-product-social-pinterest').click()
		#driver.switch_to.window()
		driver.switch_to.window(driver.window_handles[1])
		driver.find_element_by_id("email").send_keys("yzf@hotmail.com")
		#emailElement.send_keys(yzf@hotmail.com)
		driver.find_element_by_id("password").send_keys("yzf123456")
		driver.find_element_by_css_selector(".red").click()
	



		




	def tearDown(self):
		driver.quit()

if __name__ == "__main__":
   unittest.main()
