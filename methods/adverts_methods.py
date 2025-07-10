from url import TestUrl
import requests
from requests_toolbelt import MultipartEncoder

class AdvertsMethods:

    def add_advert(self, advert_data, auth_token):
        m = MultipartEncoder(fields=advert_data)
        response = requests.post(TestUrl.ADD_ADVERT_URL, data=m, headers={'Authorization': auth_token,'Content-Type': m.content_type})
        return response.status_code, response.json()

    def delete_advert(self, advert_id, auth_token):
        url = TestUrl.DELETE_ADVERT_URL + str(advert_id)
        response = requests.delete(url, headers={'Authorization': auth_token})
        return  response.status_code, response.json()

    def update_advert(self, advert_id, auth_token, new_advert_data):
        url = TestUrl.UPDATE_ADVERT_URL + str(advert_id)
        m = MultipartEncoder(fields=new_advert_data)
        response = requests.patch(url, data=m, headers={'Authorization': auth_token,'Content-Type': m.content_type})
        return response.status_code, response.json()

    def update_advert_different_user(self, advert_id, auth_token, new_advert_data):
        url = TestUrl.UPDATE_ADVERT_URL + str(advert_id)
        m = MultipartEncoder(fields=new_advert_data)