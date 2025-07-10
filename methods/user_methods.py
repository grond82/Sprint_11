from url import TestUrl
import requests

class UserMethods:

    def registration_user(self, registration_data):
        response = requests.post(TestUrl.REGISTRATE_USER_URL, data=registration_data)
        return response.status_code, response.json()

    def authorization_user(self, authorization_data):
        response = requests.post(TestUrl.AUTHORIZATION_USER_URL, data=authorization_data)
        return response.status_code, response.json()