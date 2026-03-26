import allure

from status_codes import HTTPStatusCodes


class TestGetOrderByNumber:
    @allure.title("Проверка успешного вызова метода 'Получить заказ по номеру'")
    def test_get_order_by_track_success(self, order_client, order_track):
        response = order_client.get_order_by_number(order_track)

        assert response.status_code == HTTPStatusCodes.CODE_200_OK['status_code']
        assert response.json().get('order',{}).get('track') == order_track

    @allure.title("Проверка вызова метода 'Получить заказ по номеру' с пустым заказом")
    def test_get_order_by_track_empty_number_shows_error(self, order_client):
        response = order_client.get_order_by_number("")

        assert response.status_code == HTTPStatusCodes.CODE_400_BAD_REQUEST_ACCEPT_GET['status_code']
        assert response.json().get('message') == HTTPStatusCodes.CODE_400_BAD_REQUEST_ACCEPT_GET['message']

    @allure.title("Проверка вызова метода 'Получить заказ по номеру' с несуществующим заказом")
    def test_get_order_by_track_invalid_number_shows_error(self, order_client):
        response = order_client.get_order_by_number("0")

        assert response.status_code == HTTPStatusCodes.CODE_404_NOT_FOUND_ORDER['status_code']
        assert response.json().get('message') == HTTPStatusCodes.CODE_404_NOT_FOUND_ORDER['message']
