from selenium.webdriver.common.by import By
from TestingSample.drivers.seleniumDriver import seleniumdriver
from TestingSample.drivers.webDriver import WebDriver
# from TestingSample.Pages.login.login import loginPage



class basePage(seleniumdriver):


    #----------------------  LOCATORS  ------------------------------------
    dashboard_title_xpath = "//*[contains(@class,'header-title')]//*[text()='Dashboard']"
    timeatWork_title_xpath = "//*[@class='oxd-text oxd-text--p' and text()='Time at Work']"





    def validateDashboardPageTitle(self):

        text = self.getText(self.dashboard_title_xpath, "xpath")
        self.assertionTrue("Dashboard",text, "Dashboard")




