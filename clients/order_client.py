import json

from clients.base_client import BaseClient
from endpoints import Endpoints


class OrderClient(BaseClient):
    def create_order(self, payload):
        return self.post(Endpoints.CREATE_ORDER, json.dumps(payload))

    def get_orders_list(self):
        return self.get(Endpoints.GET_ORDERS_LISR)

    def accept_order(self, order_id, courier_id):
        query_params = {"courierId": courier_id}
        return self.put(f'{Endpoints.ACCEPT_ORDER}/{order_id}', query_params)

    def get_order_by_number(self, order_id):
        query_params = {"t": order_id}
        return self.get(Endpoints.GET_ORDER_BY_NUMBER, query_params)