from selenium import webdriver


# driver = webdriver.Chrome()

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = ""
        self.timeout = 15

    def open(self):
        self.driver.maximize_window()
        self.driver.get(self.base_url)
