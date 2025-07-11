import pytest
import requests
from url import TestUrl
from data import Data

@pytest.fixture()
def get_auth_token():
    response = requests.post(TestUrl.AUTHORIZATION_USER_URL, data=Data.AUTHORIZATION_DATA_FULL)
    access_token = response.json().get('token').get('access_token')
    bearer_token = "Bearer " + access_token
    return bearer_token