from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import unittest

class CalculatorScreen():
    def __init__(self,driver):
        self.driver=driver
        self.plusButton =WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,"//div[contains(text(),'+')]")))
        self.divideButton=WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,"//div[contains(text(),'÷')]")))
        self.subButton=WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,"//tr[4]//td[4]//div[1]//div[1]")))
        self.multiButton = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//div[@aria-label='multiply']")))
        self.result=WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,"//div[@class='z7BZJb XSNERd']")))
        self.equalButton=WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,"//div[@class='XRsWPe UUhRt']")))
        # self.clearButton=WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,"//div[contains(text(),'CE')]")))

    def clickNumber(self,number):

        # for j in range(10):
        #     number1=random.randint(0,9)
        #     number2=random.randint(0,9)
        #     expectedResult=number1+number2
        number=str(number)
        for d in number:
            WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//div[@class='XRsWPe AOvabd'][contains(text()," + d + ")]"))).click()

        # enter0=driver.find_elements_by_xpath("//div[@class='XRsWPe AOvabd'][contains(text(),'0')]").click()
        # enter1=driver.find_elements_by_xpath("//div[@class='XRsWPe AOvabd'][contains(text(),'1')]").click()
        # enter2=driver.find_elements_by_xpath("//div[@class='XRsWPe AOvabd'][contains(text(),'2')]").click()
        # enter3=driver.find_elements_by_xpath("//div[@class='XRsWPe AOvabd'][contains(text(),'3')]").click()
        # enter4=driver.find_elements_by_xpath("//div[@class='XRsWPe AOvabd'][contains(text(),'4')]").click()
        # enter5=driver.find_elements_by_xpath("//div[@class='XRsWPe AOvabd'][contains(text(),'5')]").click()
        # enter6=driver.find_elements_by_xpath("//div[@class='XRsWPe AOvabd'][contains(text(),'6')]").click()
        # enter7=driver.find_elements_by_xpath("//div[@class='XRsWPe AOvabd'][contains(text(),'7')]").click()
        # enter8=driver.find_elements_by_xpath("//div[@class='XRsWPe AOvabd'][contains(text(),'8')]").click()
        # enter9=driver.find_elements_by_xpath("//div[@class='XRsWPe AOvabd'][contains(text(),'9')]").click()
        # enterDot=driver.find_elements_by_xpath("//div[@class='XRsWPe AOvabd'][contains(text(),'.')]").click()

    def addition(self,number1,number2):
        # clear result first
        # self.driver.find_element_by_xpath("//div[contains(text(),'CE')]").click()
        self.clickNumber(number1)
        self.plusButton.click()
        self.clickNumber(number2)
        self.equalButton.click()
        expectedResult = number1 + number2
        assert self.result.text==str(expectedResult)

    def division(self,number1,number2):
        # self.driver.find_element_by_xpath("//div[contains(text(),'CE')]").click()
        self.clickNumber(number1)
        self.divideButton.click()
        self.clickNumber(number2)
        self.equalButton.click()
        expectedResult = number1/number2
        assert self.result.text==str(expectedResult)

    def substraction(self,number1,number2):
        # self.driver.find_element_by_xpath("//div[contains(text(),'CE')]").click()
        self.clickNumber(number1)
        self.subButton.click()
        self.clickNumber(number2)
        self.equalButton.click()
        expectedResult = number1-number2
        assert self.result.text==str(expectedResult)

    def multiplication(self,number1,number2):
        # self.driver.find_element_by_xpath("//div[contains(text(),'CE')]").click()
        self.clickNumber(number1)
        self.multiButton.click()
        self.clickNumber(number2)
        self.equalButton.click()
        expectedResult = number1*number2
        assert self.result.text==str(expectedResult)

if __name__=="__main__":
    unittest.main()