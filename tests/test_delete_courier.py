import allure

from status_codes import HTTPStatusCodes


class TestDeleteCourier:
    @allure.title("Проверка успешного удаления курьера")
    def test_delete_courier_success(self, courier_client, courier_setup):
        response = courier_client.delete_courier(courier_setup['id'])

        assert response.status_code == HTTPStatusCodes.CODE_200_OK['status_code']
        assert response.json() == HTTPStatusCodes.CODE_200_OK['message']

    @allure.title("Проверка вызова метода 'Удалить курьер' для уже удаленного курьера")
    @allure.issue("BUG-5", "Несоответствие ответа при удалении уже удаленного курьера")
    def test_delete_courier_nonexistent_id_shows_error(self, courier_client, courier_setup):
        courier_client.delete_courier(courier_setup['id'])
        response = courier_client.delete_courier(courier_setup['id'])

        assert response.status_code == HTTPStatusCodes.CODE_404_NOT_FOUND_DELETE['status_code']
        assert response.json() == HTTPStatusCodes.CODE_404_NOT_FOUND_DELETE['message']

    @allure.title("Проверка вызова метода 'Удалить курьер' с пустым id")
    @allure.issue("BUG-6", "Несоответствие ответа при удалении курьера с пустым id")
    def test_delete_courier_without_id_shows_error(self, courier_client):
        response = courier_client.delete_courier("")

        assert response.status_code == HTTPStatusCodes.CODE_400_BAD_REQUEST_DELETE['status_code']
        assert response.json() == HTTPStatusCodes.CODE_400_BAD_REQUEST_DELETE['message']
