from selenium import webdriver
from page_yandex_find.main_page import Find_page

def test_find_yandex():

        """ Запуск Chrome. Открытие https://www.yandex.ru"""

        driver = webdriver.Chrome()
        driver.get('https://www.yandex.ru')
        print(driver.window_handles)
        driver.maximize_window()

        poisk = Find_page(driver)

        """Поиск "Planet for me" и проверка результата, переход на сайт planetfor.me и проверка результатов поиска по 
        запросу "qa" """

        poisk.yandex()
        driver.switch_to.window(driver.window_handles[1])
        poisk.input_search_planet()
        poisk.asert_qa()



