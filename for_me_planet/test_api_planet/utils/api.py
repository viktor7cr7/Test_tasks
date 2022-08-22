from utils.cheking import Cheking
from utils.https_methods import Http_methods

"""Методы для тестирования запросов  Reqres """

base_url = 'https://reqres.in'       #Базовая юрл
key = '/api/users?page=2'

class Reqres_api():

    @staticmethod
    def get_users():
        get_url = base_url + key
        print(get_url)
        result_get = Http_methods.get(get_url)

        Cheking.check_json_token(result_get, ['page', 'per_page', 'total', 'total_pages', 'data', 'support'])
        Cheking.check_email_valid(result_get)


    @staticmethod
    def post_users():

        json_body = {
    "name": "morpheus",
    "job": "leader"}

        key = '/api/users'
        post_url = base_url + key
        result_post = Http_methods.post(post_url,json_body)
        print(result_post)
        return result_post




