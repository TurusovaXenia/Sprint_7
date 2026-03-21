import pytest

from clients.couriers_client import CourierClient
from clients.order_client import OrderClient
from endpoints import Endpoints
from utils import helpers


@pytest.fixture(scope="function")
def courier_client():
    return CourierClient(Endpoints.BASE_URL)


@pytest.fixture(scope="function")
def new_courier_data(courier_client):
    new_courier_data = helpers.generate_new_courier()
    yield new_courier_data
    courier_client.delete_courier(new_courier_data["login"], new_courier_data["password"])


@pytest.fixture(scope="function")
def order_client():
    return OrderClient(Endpoints.BASE_URL)
