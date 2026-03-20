class HTTPStatusCodes:
    CODE_200_OK = {
        "status_code": 200
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

    CODE_404_NOT_FOUND = {
        "status_code": 404,
        "message": "Учетная запись не найдена"
    }