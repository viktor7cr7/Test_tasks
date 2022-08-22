from pages.login_page import Login_page
import time

from appium import webdriver

from pages.search_result_page import Search_page

"""Start session"""

desired_capabilities = {
        'platformName': "Android",
        'platformVersion': "11",
        'deviceName': "Android Emulator",
        'app': "C:\\Users\\itqa/PycharmProjects\\Test_mobile\\app_binaries\\Planet.apk"}
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=desired_capabilities)


def test_class():

    """Authorization"""

    login = Login_page(driver)
    login.authorization()

    """Find and assert"""

    search = Search_page(driver)
    search.find_and_assert()

