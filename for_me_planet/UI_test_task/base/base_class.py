
class Base():
    def __init__(self,driver):
        self.driver = driver

    """Проверка ,что результатах поиска есть https://planetfor.me ."""

    def assert_word(self,word,exp_value):
        text_word = word.text
        assert text_word == exp_value
        print('ass good')

    """Проверка наличия результатов поиска."""

    def assert_word_2(self,word,exp_value):
        text_word = word.text
        assert text_word == exp_value
        print('result good')


