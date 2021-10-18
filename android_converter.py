import unittest
from appium import webdriver
class AndroidConverter(unittest.TestCase)
    def setUp(self):
        desired_caps={}
        desired_caps['platform']='Android'
        desired_caps['platformVersion']='9.0'
        desired_caps['deviceName']='Galaxy Nexus API 28'
        desired_caps['appPackage']='com.ba.universalconverter'
        desired_caps['appActivity']='MainConverterActivity'
        desired_caps['app']='/Users/family/Desktop/android automation/features/support/PreciseUnitConversion.apk'
        self.driver=webdriver.Remote('http:localhost:4723/wd/hub',desired_caps)
        def tearDown(self):
            self.driver.quit()
        def test_converter(self):
            leftDropDown=self.driver.find_element_by_id('com.ba.universalconverter:id/select_unit_spinner')
            leftDropDown.click().select_element.select_by_text('inch')#select_element.select_by_index(0)
            # leftMenu=self.driver.find_element_by_id('com.ba.universalconverter:id/select_unit_spinner_menu_name')
            # leftMenu.gettext()
            rightDropDown=self.driver.find_element_by_id('')
            rightDropDown.click().select_element.select_by_index(0)







if __name__ == "__main__":
    unittest.main()