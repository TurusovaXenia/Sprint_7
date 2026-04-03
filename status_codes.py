class HTTPStatusCodes:
    CODE_200_OK = {
        "status_code": 200,
        "message": {'ok': True}
    }

    CODE_201_CREATED = {
        "status_code": 201,
        "message": {'ok': True}
    }

    CODE_409_CONFLICT = {
        "status_code": 409,
        "message": "Этот логин уже используется"
    }

    CODE_400_BAD_REQUEST_REGISTRATION = {
        "status_code": 400,
        "message": "Недостаточно данных для создания учетной записи"
    }

    CODE_400_BAD_REQUEST_LOGIN = {
        "status_code": 400,
        "message": "Недостаточно данных для входа"
    }

    CODE_400_BAD_REQUEST_DELETE = {
        "status_code": 400,
        "message": "Недостаточно данных для удаления курьера"
    }

    CODE_400_BAD_REQUEST_ACCEPT_GET = {
        "status_code": 400,
        "message": "Недостаточно данных для поиска"
    }

    CODE_404_NOT_FOUND_LOGIN = {
        "status_code": 404,
        "message": "Учетная запись не найдена"
    }

    CODE_404_NOT_FOUND_DELETE = {
        "status_code": 404,
        "message": "Курьера с таким id нет"
    }

    CODE_404_NOT_FOUND_ACCEPT_ORDER = {
        "status_code": 404,
        "message": "Заказа с таким id не существует"
    }

    CODE_404_NOT_FOUND_ACCEPT_COURIER = {
        "status_code": 404,
        "message": "Курьера с таким id не существует"
    }

    CODE_404_NOT_FOUND_ORDER = {
        "status_code": 404,
        "message": "Заказ не найден"
    }
