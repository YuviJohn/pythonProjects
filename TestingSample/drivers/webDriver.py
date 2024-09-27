from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager




class WebDriver():


    def setUp(self):
        url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.get(url)

        return driver