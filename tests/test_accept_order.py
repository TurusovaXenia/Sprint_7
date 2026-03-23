import pytest

from status_codes import HTTPStatusCodes


class TestAcceptOrder:
    def test_accept_order_success(self, order_client, order_setup, courier_setup):
        response = order_client.accept_order(order_setup, courier_setup['id'])

        assert response.status_code == HTTPStatusCodes.CODE_200_OK['status_code']
        assert response.json() == HTTPStatusCodes.CODE_200_OK['message']

    @pytest.mark.parametrize("order_id_idx, courier_id_idx, expected_error", [
        ("", "valid", HTTPStatusCodes.CODE_400_BAD_REQUEST_ACCEPT_GET),
        ("valid", "", HTTPStatusCodes.CODE_400_BAD_REQUEST_ACCEPT_GET),
        ("-1", "valid", HTTPStatusCodes.CODE_404_NOT_FOUND_ACCEPT_ORDER),
        ("valid", "-1", HTTPStatusCodes.CODE_404_NOT_FOUND_ACCEPT_COURIER),
    ], ids=["empty_order_id_shows_error",
            "empty_courier_id_shows_error",
            "invalid_order_id_shows_error",
            "invalid_courier_id_shows_error"]
                             )
    def test_accept_order(self, order_client, order_setup, order_id_idx,
                          courier_setup, courier_id_idx,
                          expected_error):
        order_id = order_setup if order_id_idx == "valid" else order_id_idx
        courier_id = courier_setup["id"] if courier_id_idx == "valid" else courier_id_idx

        response = order_client.accept_order(order_id, courier_id)

        assert response.status_code == expected_error['status_code']
        assert response.json() == expected_error['message']
