from TestingSample.drivers.webDriver import WebDriver
from TestingSample.Pages.homePage import basePage
# from TestingSample.drivers.seleniumDriver import seleniumdriver
from selenium.webdriver.common.by import By

import time






class loginPage(basePage):

    #Locators

    username_editbox_name = "username"
    password_editbox_name = "password"
    login_button_xpath =  "//*[contains(@class, 'login-button')]"

    # def __init__(self):
    #     self.bp = basePage()

    def enterUsername(self, username):
        # time.sleep(15)
        self.sendKeys(self.username_editbox_name, "name", username)

    def enterPassword(self, password):
        # time.sleep(5)
        self.sendKeys(self.password_editbox_name, "name", password)

    def clickLogin(self):
        # time.sleep(5)
        self.clickElement(self.login_button_xpath, "xpath")


    def login(self, username, password):
        time.sleep(15)
        self.enterUsername(username)
        time.sleep(2)
        self.enterPassword(password)
        time.sleep(2)
        self.clickLogin()
        time.sleep(15)
        self.validateDashboardPageTitle()

