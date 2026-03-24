import allure
import pytest

from status_codes import HTTPStatusCodes


class TestAcceptOrder:
    @allure.title("Проверка успешного вызова метода 'Принять заказ'")
    @allure.issue("BUG-7", "нестабильный ответ 404 Not Found (Flaky) при вызове метода 'Принять заказ'")
    def test_accept_order_success(self, order_client, order_track, courier_setup):
        response = order_client.accept_order(order_track, courier_setup['id'])

        assert response.status_code == HTTPStatusCodes.CODE_200_OK['status_code']
        assert response.json() == HTTPStatusCodes.CODE_200_OK['message']

    @pytest.mark.parametrize("order_track_x, courier_id_idx, expected_error", [
        pytest.param(
            "", "valid", HTTPStatusCodes.CODE_400_BAD_REQUEST_ACCEPT_GET,
            marks=[
                allure.issue("BUG-8", "несоответствие ответа при принятии заказа с пустым id"),
            ],
            id="empty_order_id_shows_error",
        ),
        pytest.param(
            "valid", "", HTTPStatusCodes.CODE_400_BAD_REQUEST_ACCEPT_GET,
            marks=[
                allure.issue("BUG-9",
                             "лишнее поле 'code' в ответе метода 'Принять заказ' если параметр courier_id пустой или невалиден")
            ],
            id="empty_courier_id_shows_error"
        ),
        pytest.param(
            "-1", "valid", HTTPStatusCodes.CODE_404_NOT_FOUND_ACCEPT_ORDER,
            marks=[
                allure.issue("BUG-10",
                             "лишнее поле 'code' в ответе метода 'Принять заказ' если параметр id невалиден")
            ],
            id="invalid_order_id_shows_error"
        ),
        pytest.param(
            "valid", "-1", HTTPStatusCodes.CODE_404_NOT_FOUND_ACCEPT_COURIER,
            marks=[
                allure.issue("BUG-9", "лишнее поле 'code' в ответе метода 'Принять заказ' если параметр courier_id пустой или невалиден")
            ],
            id="invalid_courier_id_shows_error"
        ),
    ])
    @allure.title("Проверка негативных сценариев для метода 'Принять заказ'")
    @allure.description("Происходит проверка четырех кейсов - пустой order_track/courier_id, невалидный order_track/courier_id")
    def test_accept_order(self, order_client, order_track, order_track_x,
                          courier_setup, courier_id_idx,
                          expected_error):
        order = order_track if order_track_x == "valid" else order_track_x
        courier_id = courier_setup["id"] if courier_id_idx == "valid" else courier_id_idx

        response = order_client.accept_order(order, courier_id)

        assert response.status_code == expected_error['status_code']
        assert response.json() == expected_error['message']
