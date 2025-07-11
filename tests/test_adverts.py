import pytest
from methods.adverts_methods import AdvertsMethods
from data import Data


class TestAdverts:

    @pytest.mark.parametrize(
        'advert_data',
        [
            Data.DATA_ADVERT_1,
            Data.DATA_ADVERT_2,
            Data.DATA_ADVERT_3,
            Data.DATA_ADVERT_4,
            Data.DATA_ADVERT_5
        ]
    )
    def test_create_advert(self, get_auth_token, advert_data):
        advert_methods = AdvertsMethods()
        auth_token = get_auth_token
        status_code, text= advert_methods.add_advert(advert_data, auth_token)
        assert status_code == 201

    def test_delete_advert(self, get_auth_token):
        advert_methods = AdvertsMethods()
        auth_token = get_auth_token
        _, text = advert_methods.add_advert(Data.DATA_ADVERT_5, auth_token)
        advert_id = text.get("id")
        status_code, text = advert_methods.delete_advert(advert_id,auth_token)
        assert status_code == 200 and text.get("message") == Data.MESSAGE_DELETE_ADVERT

    def test_update_advert(self, get_auth_token):
        advert_methods = AdvertsMethods()
        auth_token = get_auth_token
        _, text = advert_methods.add_advert(Data.DATA_ADVERT_1, auth_token)
        advert_id = text.get("id")
        status_code,_ = advert_methods.update_advert(advert_id,auth_token,Data.DATA_UPDATE_ADVERT_1)
        assert status_code == 200

    def test_update_advert_different_user(self, get_auth_token):
        advert_methods = AdvertsMethods()
        auth_token = get_auth_token
        advert_id = Data.ID_DIFFERENT_USER_ADVERT
        status_code, text = advert_methods.update_advert(advert_id, auth_token, Data.DATA_UPDATE_ADVERT_1)
        assert status_code == 401 and text.get("message") == Data.MESSAGE_UPDATE_DIFFERENT_USER_ADVERT