from utils.api import Reqres_api

from requests import Response

from utils.cheking import Cheking

"""Тест для проверки наличия полей в ответе и валидации e-mail"""

class Test_get_request():

    def test_get_req(self):
        print("Method  GET")

        result_get: Response = Reqres_api.get_users()

    '''Тест для проверки значений в ответе '''

    def test_post_req(self):
        print('Method POST')

        result_post: Response = Reqres_api.post_users()

        Cheking.check_value_json(result_post, 'name', 'morpheus')

        Cheking.check_value_json(result_post, 'job', 'leader')


