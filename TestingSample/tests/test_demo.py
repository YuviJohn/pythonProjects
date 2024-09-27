from TestingSample.drivers.webDriver import WebDriver
from TestingSample.Pages.login.login import loginPage
from TestingSample.Pages.homePage import basePage
import time
import pytest
import logging


class TestCases():


    @pytest.fixture(autouse=True)
    def setUp(self):
        self.login = loginPage()
        # self.bp = basePage()

    @pytest.mark.run(order=2)
    def test_case01(self):
        # time.sleep(30)
        self.login.login("Admin", "admin12")

    @pytest.mark.run(order=1)
    def test_case02(self):

        a = 10
        b= 20
        print(a+b)