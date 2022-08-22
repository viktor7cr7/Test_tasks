from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base_1
from selenium.webdriver.support import expected_conditions as EC

class Search_page(Base_1):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver


    #locators

    click_search = 'com.planet.forme:id/navigationGlobalSearch'
    input_search = 'com.planet.forme:id/searchEditText'
    result_search = 'com.planet.forme:id/tvReviewName'


    #Getters

    def get_search(self):
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.ID, self.click_search)))

    def get_input_search(self):
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.ID, self.input_search)))



    def get_no_resuslt_search(self):
        return WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.ID, self.result_search)))



    #Action

    def click_on_search(self):
        self.get_search().click()

    def search_input(self):
        self.get_input_search().send_keys('Москва')


    def find_and_assert(self):
        self.click_on_search()
        self.search_input()
        self.assert_find(self.get_no_resuslt_search(),'Москва')









