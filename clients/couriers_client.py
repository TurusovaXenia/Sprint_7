from clients.base_client import BaseClient
from endpoints import Endpoints
from status_codes import HTTPStatusCodes


class CourierClient(BaseClient):
    def create_courier(self, payload):
        return self.post(Endpoints.CREATE_COURIER, payload)

    def login_courier(self, login, password):
        payload = {
            'login': login,
            'password': password
        }
        return self.post(Endpoints.LOGIN_COURIER, payload)

    def delete_courier(self, login, password):
        response = self.login_courier(login, password)
        if response.status_code == HTTPStatusCodes.CODE_200_OK:
            courier_id = response.json()['id']
            self.delete(f'{Endpoints.DELETE_COURIER}/{courier_id}')
