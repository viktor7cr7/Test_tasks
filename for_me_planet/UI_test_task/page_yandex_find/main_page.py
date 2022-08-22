from selenium.webdriver import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from base.base_class import Base
import time
from selenium.webdriver.support import expected_conditions as EC

class Find_page(Base):

    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver


    # Locators

    find_yandex = "//input[@class='input__control input__input mini-suggest__input']"
    button_find_yandex = "//button[@class='button mini-suggest__button button_theme_search button_size_search i-bem button_js_inited']"
    text_planet = "//div/div/a/b[text()='planetfor.me']"
    search_planeta = "//input[@type='search']"

    # Getters

    def get_find_yandex(self):
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH, self.find_yandex)))

    def get_button_yandex(self):
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH, self.button_find_yandex)))

    def get_text_planet(self):
        return WebDriverWait(self.driver,30).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="search-result"]/li[2]/div/div[2]/div[1]/a')))

    def check_text_planet(self):
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH, self.text_planet)))

    def get_search_planeta(self):
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH, self.search_planeta)))

    def get_no_result_search(self):
        return WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/a/div/div[2]/div[1]/p')))



    # Actions

    def input_find_yandex(self):
        self.get_find_yandex().send_keys('Planet for me')

    def click_button_yandex(self):
        self.get_button_yandex().click()

    def assertion_word(self):
        self.assert_word(self.get_text_planet(),'planetfor.me')

    def click_text_planet(self):
        self.check_text_planet().click()

    def input_search_planet(self):
        self.get_search_planeta().send_keys('qa',Keys.ENTER)

    def asert_qa(self):
        self.assert_word_2(self.get_no_result_search(),'qawsedrf1234')


    def yandex(self):
        self.input_find_yandex()
        self.click_button_yandex()
        self.click_text_planet()
        self.assertion_word()
        time.sleep(2)
