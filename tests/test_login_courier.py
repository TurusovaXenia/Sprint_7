import allure
import pytest

import data
from status_codes import HTTPStatusCodes


class TestLoginCourier:
    @allure.title("Проверка успешного входа курьера")
    def test_login_courier_success(self, courier_client, courier_setup):
        response = courier_client.login_courier(courier_setup["login"], courier_setup["password"])

        assert response.status_code == HTTPStatusCodes.CODE_200_OK["status_code"]
        assert "id" in response.json()

    @allure.title("Проверка вызова 'Логин курьера в системе' с пустым имейлом/паролем")
    @allure.issue("BUG-3",
                  "лишнее поле 'code' в ответе метода 'Логин курьера в систему' при входе с пустым логином или паролем")
    @pytest.mark.parametrize("empty_field", ["login", "password"])
    def test_login_courier_empty_fields_show_error(self, courier_client, empty_field):
        courier_data = data.valid_courier_data.copy()
        courier_data[empty_field] = ''
        response = courier_client.login_courier(courier_data["login"], courier_data["password"])

        assert response.status_code == HTTPStatusCodes.CODE_400_BAD_REQUEST_LOGIN['status_code']
        assert response.json() == HTTPStatusCodes.CODE_400_BAD_REQUEST_LOGIN['message']

    @allure.title("Проверка вызова 'Логин курьера в системе' с невалидным имейлом/паролем")
    @allure.issue("BUG-4",
                  "лишнее поле 'code' в ответе метода 'Логин курьера в систему' при входе с невалидным логином или паролем")
    @pytest.mark.parametrize("incorrect_field", ["login", "password"])
    def test_login_courier_incorrect_fields_show_error(self, courier_client, incorrect_field):
        courier_data = data.valid_courier_data.copy()
        courier_data[incorrect_field] = f"incorrect {incorrect_field}"
        response = courier_client.login_courier(courier_data["login"], courier_data["password"])

        assert response.status_code == HTTPStatusCodes.CODE_404_NOT_FOUND_LOGIN['status_code']
        assert response.json() == HTTPStatusCodes.CODE_404_NOT_FOUND_LOGIN['message']

    @allure.title("Проверка вызова 'Логин курьера в системе' для несуществующего пользователя")
    @allure.issue("BUG-4",
                  "лишнее поле 'code' в ответе метода 'Логин курьера в систему' при входе с невалидным логином или паролем")
    def test_login_courier_nonexistent_courier_show_error(self, courier_client, new_courier_data):
        response = courier_client.login_courier(new_courier_data["login"], new_courier_data["password"])

        assert response.status_code == HTTPStatusCodes.CODE_404_NOT_FOUND_LOGIN['status_code']
        assert response.json() == HTTPStatusCodes.CODE_404_NOT_FOUND_LOGIN['message']
