import random
import string

class Helpers:

    @staticmethod
    def generate_new_user_param():
        def generate_random_yandex_email(length):
            letters = string.ascii_lowercase
            random_string = ''.join(random.choice(letters) for i in range(length))
            random_string = random_string + '@yandex.ru'
            return random_string
        def generate_random_string(length):
            letters = string.ascii_lowercase
            random_string = ''.join(random.choice(letters) for i in range(length))
            return random_string
        email = generate_random_yandex_email(10)
        password = generate_random_string(5)
        payload = {
            "email": email,
            "password": password,
            "submitPassword": password
        }
        return payload