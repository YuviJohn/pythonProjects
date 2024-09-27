from pandas.core.arrays import boolean
from selenium.common import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver.support.wait import WebDriverWait

from TestingSample.drivers.webDriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains
from TestingSample.utility.utilities import utility
from TestingSample.utility.logger import logs
from selenium.webdriver.support import expected_conditions as EC






class seleniumdriver(utility):



    def __init__(self):
        self.driver = WebDriver.setUp(self)
        self.log = logs.logging(self)

    def getByType(self, locatorType):
        locatorType = locatorType.lower()
        try:
            if locatorType == "id":
                return By.ID
            elif locatorType == "name":
                return By.NAME
            elif locatorType == "xpath":
                return By.XPATH
            elif locatorType == "css":
                return By.CSS_SELECTOR
            elif locatorType == "class":
                return By.CLASS_NAME
            elif locatorType == "linktext":
                return By.LINK_TEXT
            elif locatorType == "tagname":
                return By.TAG_NAME
            self.log.info("*** Element has been identified using BY Type " + locatorType + "****")
        except:
            self.log.info("*** Element is not identified using BY Type " + locatorType + "****")

    # ---------------- CUSTOM GET ELEMENT ----------------------------
    def getElement(self, locator, locatorType):
        element = ""
        try:
            Actual_Value = True
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_element(byType, locator)
            self.log.info("*** ELEMENT HAS BEEN IDENTIFIED SUCCESSFULLY " + locator + " with " + locatorType)
        except:
            self.log.error("*** ELEMENT IS NOT IDENTIFIED " + locator + " with " + locatorType)

        return element

    def sendKeys(self, locator, locatorType, value):
        try:
            element = self.getElement(locator, locatorType)
            element.send_keys(value)
            self.log.info("**** Value has been sent to the element " + locator + " with " + locatorType + "****")
        except:
            self.log.error("**** Value was not able to send to the element " + locator + " with " + locatorType + "****")

    def clickElement(self, locator, locatorType):

        element = self.getElement(locator, locatorType)
        element.send_keys(Keys.RETURN)


    def getText(self, locator, locatorType):
        text = ""
        element = self.getElement(locator, locatorType)
        # txt = element.text
        txt = element.get_attribute("innerText")
        return txt

    def selectByText(self, locator, locatorType, txtValue):

        element = self.getElement(locator, locatorType)
        option = Select(element)
        option.select_by_visible_text(txtValue)

    def selectByValue(self, locator, locatorType, txtValue):

        element = self.getElement(locator, locatorType)
        option = Select(element)
        option.select_by_value(txtValue)

    def selectByIndex(self, locator, locatorType, txtValue):

        element = self.getElement(locator, locatorType)
        option = Select(element)
        option.select_by_index(txtValue)

    def moveToElement(self,locator, locatorType):

        element = self.getElement(locator, locatorType)
        action = ActionChains(self.driver)
        action.move_to_element(element)

    def clickElementAction(self,locator, locatorType):

        element = self.getElement(locator, locatorType)
        action = ActionChains(self.driver)
        action.move_to_element(element).click().perform()

    def doublclickElement(self,locator, locatorType):

        element = self.getElement(locator, locatorType)
        action = ActionChains(self.driver)
        action.move_to_element(element).double_click().perform()

    def WaitForElement(self, locator, locatorType):

        wait = WebDriverWait(self.driver,timeout=10,poll_frequency=0.5,ignored_exceptions=[NoSuchElementException,
                                                                                           ElementNotVisibleException,
                                                                                           ElementNotSelectableException])

        wait.until(EC.element_to_be_clickable(self.getByType(locator, locatorType)))