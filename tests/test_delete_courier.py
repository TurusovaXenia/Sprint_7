from status_codes import HTTPStatusCodes


class TestDeleteCourier:
    def test_delete_courier_success(self, courier_client, courier_setup):
        response = courier_client.delete_courier(courier_setup['id'])

        assert response.status_code == HTTPStatusCodes.CODE_200_OK['status_code']
        assert response.json() == HTTPStatusCodes.CODE_200_OK['message']

    def test_delete_courier_nonexistent_id_shows_error(self, courier_client, courier_setup):
        courier_client.delete_courier(courier_setup['id'])
        response = courier_client.delete_courier(courier_setup['id'])

        assert response.status_code == HTTPStatusCodes.CODE_404_NOT_FOUND_DELETE['status_code']
        assert response.json() == HTTPStatusCodes.CODE_404_NOT_FOUND_DELETE['message']

    def test_delete_courier_without_id_shows_error(self, courier_client):
        response = courier_client.delete_courier("")

        assert response.status_code == HTTPStatusCodes.CODE_400_BAD_REQUEST_DELETE['status_code']
        assert response.json() == HTTPStatusCodes.CODE_400_BAD_REQUEST_DELETE['message']
