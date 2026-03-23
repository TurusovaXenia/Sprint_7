import pytest

import data
from clients.couriers_client import CourierClient
from clients.order_client import OrderClient
from endpoints import Endpoints
from status_codes import HTTPStatusCodes
from utils import helpers


@pytest.fixture(scope="function")
def courier_client():
    return CourierClient(Endpoints.BASE_URL)


@pytest.fixture(scope="function")
def new_courier_data():
    new_courier_data = helpers.generate_new_courier()
    return new_courier_data


@pytest.fixture(scope="function")
def courier_cleanup(courier_client, new_courier_data):
    yield new_courier_data
    response = courier_client.login_courier(new_courier_data["login"], new_courier_data["password"])
    if response.status_code == HTTPStatusCodes.CODE_200_OK['status_code']:
        courier_id = response.json()["id"]
        courier_client.delete_courier(courier_id)


@pytest.fixture(scope="function")
def order_client():
    return OrderClient(Endpoints.BASE_URL)


@pytest.fixture(scope="function")
def courier_setup(courier_client, new_courier_data):
    courier_client.create_courier(new_courier_data)
    response = courier_client.login_courier(new_courier_data["login"], new_courier_data["password"])
    courier_id = response.json()["id"]

    setup_data = {
        "id": courier_id,
        "login": new_courier_data["login"],
        "password": new_courier_data["password"],
    }
    yield setup_data

    if courier_id:
        courier_client.delete_courier(courier_id)


@pytest.fixture(scope="function")
def order_setup(order_client):
    response = order_client.create_order(data.order_data)
    order_id = response.json()["track"]
    return order_id
