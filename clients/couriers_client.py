import allure

from clients.base_client import BaseClient
from endpoints import Endpoints


class CourierClient(BaseClient):
    @allure.step("Отправка POST-запроса для создания курьера")
    def create_courier(self, payload):
        return self.post(Endpoints.CREATE_COURIER, payload)

    @allure.step("Отправка POST-метода для логина курьера")
    def login_courier(self, login, password):
        payload = {
            'login': login,
            'password': password
        }
        return self.post(Endpoints.LOGIN_COURIER, payload)

    @allure.step("Отправка DELETE-запроса для удаления курьера")
    def delete_courier(self, courier_id):
        return self.delete(f'{Endpoints.DELETE_COURIER}/{courier_id}')
