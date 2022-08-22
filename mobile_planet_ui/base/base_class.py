class Base_1():
    def __init__(self,driver):
        self.driver = driver



 # """Method assert find"""


    def assert_find(self,word,result):
        value_word = word.text
        assert value_word == result
        print("Have result")

