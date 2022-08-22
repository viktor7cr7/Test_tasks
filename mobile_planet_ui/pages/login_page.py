import time
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC
from base.base_class import Base_1


class Login_page(Base_1):
    def __init__(self,driver):
        super().__init__(driver)

        self.driver = driver

    #locators



    login_switch = 'com.planet.forme:id/logInTabButton'

    user_name = 'com.planet.forme:id/loginInput'

    password_name = 'com.planet.forme:id/passwordInput'

    click_login = 'com.planet.forme:id/signInButton'



    #Getters

    def get_switch_login(self):
        return WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.ID, self.login_switch)))

    def get_user_name(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.ID, self.user_name)))

    def get_password_name(self):
        return WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.ID, self.password_name)))

    def get_click_login(self):
        return WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.ID, self.click_login)))



    #Action

    def swith_to_login(self):
        self.get_switch_login().click()

    def input_user_name(self):
        self.get_user_name().send_keys('carlotest')

    def input_password_name(self):
        self.get_password_name().send_keys('BETejEmm321')

    def click_to_login(self):
        self.get_click_login().click()


    #Method


    def authorization(self):

        self.swith_to_login()
        self.input_user_name()
        self.input_password_name()
        self.click_to_login()







