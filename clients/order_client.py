import json

import allure

from clients.base_client import BaseClient
from endpoints import Endpoints


class OrderClient(BaseClient):
    @allure.step("Отправка POST-запроса для создания заказа")
    def create_order(self, payload):
        return self.post(Endpoints.CREATE_ORDER, json.dumps(payload))

    @allure.step("Отправка GET-запроса для получения списка заказов")
    def get_orders_list(self):
        return self.get(Endpoints.GET_ORDERS_LISR)

    @allure.step("Отправка PUT-запроса для подтверждения заказа")
    def accept_order(self, order_id, courier_id):
        query_params = {"courierId": courier_id}
        return self.put(f'{Endpoints.ACCEPT_ORDER}/{order_id}', query_params)

    @allure.step("Отправка GET-запроса для получения заказа по трек-номеру")
    def get_order_by_number(self, order_id):
        query_params = {"t": order_id}
        return self.get(Endpoints.GET_ORDER_BY_NUMBER, query_params)