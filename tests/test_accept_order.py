import allure
import pytest

from status_codes import HTTPStatusCodes


class TestAcceptOrder:
    @allure.title("Проверка успешного вызова метода 'Принять заказ'")
    @allure.issue("BUG-4", "нестабильный ответ 404 Not Found (Flaky) при вызове метода 'Принять заказ'")
    def test_accept_order_success(self, order_client, order_track, courier_setup):
        response = order_client.accept_order(order_track, courier_setup['id'])

        assert response.status_code == HTTPStatusCodes.CODE_200_OK['status_code']
        assert response.json() == HTTPStatusCodes.CODE_200_OK['message']

    @allure.title("Проверка неуспешный кейсов для параметра id метода 'Принять заказ'")
    @allure.issue("BUG-5", "несоответствие ответа метода 'Принять заказ' при работе с пустым 'id'")
    @pytest.mark.parametrize("order_track, expected_error", [
        ("", HTTPStatusCodes.CODE_400_BAD_REQUEST_ACCEPT_GET),
        ("-1", HTTPStatusCodes.CODE_404_NOT_FOUND_ACCEPT_ORDER)
    ], ids=[
        "empty_order_id_shows_error", "invalid_order_id_shows_error"
    ])
    def test_accept_order_order_validation(self, order_client, courier_setup, order_track,
                                           expected_error):
        response = order_client.accept_order(order_track, courier_setup['id'])

        assert response.status_code == expected_error['status_code']
        assert response.json().get('message') == expected_error['message']

    @allure.title("Проверка неуспешный кейсов для параметра courier_id метода 'Принять заказ'")
    @pytest.mark.parametrize("courier_id, expected_error", [
        ("", HTTPStatusCodes.CODE_400_BAD_REQUEST_ACCEPT_GET),
        ("-1", HTTPStatusCodes.CODE_404_NOT_FOUND_ACCEPT_COURIER),
    ], ids=[
        "empty_courier_id_shows_error", "invalid_courier_id_shows_error"
    ])
    def test_accept_order_courier_validation(self, order_client, order_track, courier_id,
                                             expected_error):
        response = order_client.accept_order(order_track, courier_id)

        assert response.status_code == expected_error['status_code']
        assert response.json().get('message') == expected_error['message']
