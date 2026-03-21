from status_codes import HTTPStatusCodes


class TestGetOrdersList:
    def test_get_orders_list_success(self, order_client):
        response = order_client.get_orders_list()
        assert response.status_code == HTTPStatusCodes.CODE_200_OK['status_code']
        assert "orders" in response.json()
