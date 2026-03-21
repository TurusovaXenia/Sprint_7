from clients.base_client import BaseClient
from endpoints import Endpoints


class OrderClient(BaseClient):
    def create_order(self, payload):
        return self.post(Endpoints.CREATE_ORDER, payload)

    def get_orders_list(self):
        return self.get(Endpoints.GET_ORDERS_LISR)