from selenium import webdriver
from selenium.webdriver.common.by import By
from common.BasePage import BasePage


# PageObject 设计模式原理:将页面的元素定位和元素行为封装成一个page类。一个页面对应一个类。
# https://blog.csdn.net/qq_44614026/article/details/108938337

class LoginPage(BasePage):

    # def __init__(self, driver):
    #     self.driver = driver

    # 页面元素
    username_input = (By.XPATH, "")
    pwd_input = (By.XPATH, "")
    login_btn = (By.XPATH, "")

    # 页面行为
    def login(self, username, password):
        self.driver.find_element(self.username_input).send_keys(username)
        self.driver.find_element(self.pwd_input).send_keys(password)
        self.driver.find_element(self.login_btn).click()
