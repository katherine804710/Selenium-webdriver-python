from selenium import webdriver
import unittest
from pages.calculator_screen import CalculatorScreen

class CalculatorTest(unittest.TestCase):

    def setUp(self):
        global driver
        driver = webdriver.Firefox(executable_path='/Users/family/Downloads/geckodriver')
        driver.get("https://www.google.com/search?client=firefox-b-1-d&nfpr=1&sxsrf=ALeKk02vfzul4Gz8K2E0dN-gpkyxMuOMKQ:1584837474822&q=calculator&spell=1&sa=X&ved=2ahUKEwjEotrV66zoAhXTvZ4KHa5wAdcQBSgAegQICxAn&biw=1398&bih=787")

    def test_addition(self):
        #the "CE" button only delete one number so i use driver.get to refresh page for each function
        driver.get("https://www.google.com/search?client=firefox-b-1-d&nfpr=1&sxsrf=ALeKk02vfzul4Gz8K2E0dN-gpkyxMuOMKQ:1584837474822&q=calculator&spell=1&sa=X&ved=2ahUKEwjEotrV66zoAhXTvZ4KHa5wAdcQBSgAegQICxAn&biw=1398&bih=787")
        calculator=CalculatorScreen(driver)
        calculator.addition(2,2)
        # self.driver.find_element_by_name("2").click()
        # self.driver.find_element_by_name("+").click()
        # self.driver.find_element_by_name("2").click()
        # self.driver.find_element_by_name("=").click()
        # test_addition(2,2)
        # value = self.driver.find_element_by_id("result").get_attribute("value")
        # self.assertEqual('4', value)

    def test_division(self):
        driver.get("https://www.google.com/search?client=firefox-b-1-d&nfpr=1&sxsrf=ALeKk02vfzul4Gz8K2E0dN-gpkyxMuOMKQ:1584837474822&q=calculator&spell=1&sa=X&ved=2ahUKEwjEotrV66zoAhXTvZ4KHa5wAdcQBSgAegQICxAn&biw=1398&bih=787")
        calculator=CalculatorScreen(driver)
        calculator.division(5,2)

    def test_multiplication(self):
        driver.get("https://www.google.com/search?client=firefox-b-1-d&nfpr=1&sxsrf=ALeKk02vfzul4Gz8K2E0dN-gpkyxMuOMKQ:1584837474822&q=calculator&spell=1&sa=X&ved=2ahUKEwjEotrV66zoAhXTvZ4KHa5wAdcQBSgAegQICxAn&biw=1398&bih=787")
        calculator=CalculatorScreen(driver)
        calculator.multiplication(8,2)

    def test_substraction(self):
        driver.get("https://www.google.com/search?client=firefox-b-1-d&nfpr=1&sxsrf=ALeKk02vfzul4Gz8K2E0dN-gpkyxMuOMKQ:1584837474822&q=calculator&spell=1&sa=X&ved=2ahUKEwjEotrV66zoAhXTvZ4KHa5wAdcQBSgAegQICxAn&biw=1398&bih=787")
        calculator=CalculatorScreen(driver)
        calculator.substraction(100,1)

    def tearDown(self):
        driver.quit()
if __name__=="__main__":
    unittest.main()