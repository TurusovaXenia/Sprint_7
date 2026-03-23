import pytest

import data
from status_codes import HTTPStatusCodes


class TestCreateOrder:
    @pytest.mark.parametrize("color", ["BLACK", "GREY", ["BLACK", "GREY"], []])
    def test_create_order_success(self, order_client, color):
        order_data = data.order_data.copy()
        order_data["color"] = color
        response = order_client.create_order(order_data)

        assert response.status_code == HTTPStatusCodes.CODE_201_CREATED['status_code']
        assert "track" in response.json()
