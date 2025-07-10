from methods.user_methods import UserMethods
from data import Data
from helpers import Helpers

class TestUser:

    def test_registration_user(self):
        helpers_methods = Helpers()
        registration_data = helpers_methods.generate_new_user_param()
        user_methods = UserMethods()
        status_code,_ = user_methods.registration_user(registration_data)
        assert status_code == 201

    def test_registration_same_user(self):
        helpers_methods = Helpers()
        registration_data = helpers_methods.generate_new_user_param()
        user_methods = UserMethods()
        user_methods.registration_user(registration_data)
        status_code, text = user_methods.registration_user(registration_data)
        assert status_code == 400 and text.get('message') == Data.MESSAGE_CREATE_SAME_COURIER

    def test_authorization_user(self):
        user_methods = UserMethods()
        status_code, _ = user_methods.authorization_user(Data.AUTHORIZATION_DATA_FULL)
        assert status_code == 201