import json
from requests import Response
import re
class Cheking():


    """Проверка наличия полей в ответе запроса"""

    @staticmethod
    def check_json_token(response: Response, expected_value):
        token = json.loads(response.text)
        assert list(token) == expected_value
        print('All fields are present')


    """Проверка валидации поля email"""

    @staticmethod
    def check_email_valid(response: Response):
        token = json.loads(response.text)
        check_email = [tqe.get('email') for tqe in token['data']]
        print(check_email)
        for zet in check_email:
            print(zet)
        text_reg = r"@\w+\."
        fin_reg = re.findall(text_reg,zet)
        print(fin_reg)

        assert check_email[1] == 'lindsay.' + 'ferguson' + '@' + 'reqres.in'
        print('Check e-mail pass')


    """Проверка что значения в ответе те же, что и были в запросе"""

    @staticmethod
    def check_value_json(response: Response, field_name, expected_value):
        check = response.json()
        check_info = check.get(field_name)
        assert check_info == expected_value
        print('поле ' + field_name + ' Верное')





