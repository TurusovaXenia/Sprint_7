from status_codes import HTTPStatusCodes


class TestGetOrderByNumber():
    def test_get_order_by_number_success(self, order_client, order_setup):
        response = order_client.get_order_by_number(order_setup)

        assert response.status_code == HTTPStatusCodes.CODE_200_OK['status_code']
        assert response.json()['order']['track'] == order_setup

    def test_get_order_by_number_empty_number_shows_error(self, order_client):
        response = order_client.get_order_by_number("")

        assert response.status_code == HTTPStatusCodes.CODE_400_BAD_REQUEST_ACCEPT_GET['status_code']
        assert response.json() == HTTPStatusCodes.CODE_400_BAD_REQUEST_ACCEPT_GET['message']

    def test_get_order_by_number_invalid_number_shows_error(self, order_client):
        response = order_client.get_order_by_number("0")

        assert response.status_code == HTTPStatusCodes.CODE_404_NOT_FOUND_ORDER['status_code']
        assert response.json() == HTTPStatusCodes.CODE_404_NOT_FOUND_ORDER['message']
