import allure
import pytest

import data
from status_codes import HTTPStatusCodes


class TestCreateCourier:
    @allure.title("Проверка успешного создания курьера")
    def test_create_courier_success(self, courier_client, new_courier_data, courier_cleanup):
        response = courier_client.create_courier(new_courier_data)

        assert response.status_code == HTTPStatusCodes.CODE_201_CREATED['status_code']
        assert response.json() == HTTPStatusCodes.CODE_201_CREATED['message']

    @allure.title("Проверка невозможности создания двух курьеров с одинаковыми данными")
    def test_create_courier_duplicate_shows_error(self, courier_client, new_courier_data, courier_cleanup):
        courier_client.create_courier(new_courier_data)
        response = courier_client.create_courier(new_courier_data)

        assert response.status_code == HTTPStatusCodes.CODE_409_CONFLICT['status_code']
        assert response.json() == HTTPStatusCodes.CODE_409_CONFLICT['message']

    @pytest.mark.parametrize("empty_field", ["login", "password"])
    @allure.title("Проверка невозможности создания курьера если обязательные поля отсутствуют в запросе")
    def test_create_courier_empty_fields_shows_error(self, courier_client, empty_field):
        courier_data = data.valid_courier_data.copy()
        courier_data[empty_field] = ''
        response = courier_client.create_courier(courier_data)

        assert response.status_code == HTTPStatusCodes.CODE_400_BAD_REQUEST_REGISTRATION['status_code']
        assert response.json() == HTTPStatusCodes.CODE_400_BAD_REQUEST_REGISTRATION['message']
