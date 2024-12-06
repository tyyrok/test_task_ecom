import httpx


FIRST_REQUEST_BODY = {"user_phone": "2020-12-02", "user_date": "email@mail.ru"}
SECOND_REQUEST_BODY = {
    "user_phone": "+79141231233",
    "user_date": "email@mail.ru",
}
URL = "http://127.0.0.1:8000/v1/get_form/"


def make_request(body: dict) -> dict:
    return httpx.post(URL, json=body)


if __name__ == "__main__":
    # Получаем имя найденного шаблона формы
    res: httpx.Response = make_request(FIRST_REQUEST_BODY)
    assert "name" in res.json()

    # Форма не найдена, получаем данные c типами
    res: httpx.Response = make_request(SECOND_REQUEST_BODY)
    res = res.json()
    assert "name" not in res
    assert "phone" in res.values()
    assert "email" in res.values()
    assert "text" not in res.values()
