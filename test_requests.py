import requests
from urllib.parse import urljoin


URL = "http://localhost:8000"
ENDPOINT = "get_form"

TEMPLATE_FORM = {"user": "value", "ordered": "2024-12-12"}

UNKNOWN_FORM = {"wrong_key": "value", "ordered": "2024-12-12"}


def test_template():
    url = urljoin(URL, ENDPOINT)
    params = TEMPLATE_FORM
    response = requests.post(url=url, params=params)
    assert response.json() == {"template_name": "Order"}
    print("test_template passed")


def test_unknown_form():
    url = urljoin(URL, ENDPOINT)
    params = UNKNOWN_FORM
    response = requests.post(url=url, params=params)
    assert response.json() == {"wrong_key": "text", "ordered": "date"}
    print("test_unknown_form passed")


if __name__ == "__main__":
    test_template()
    test_unknown_form()
    print("All tests passed!")
