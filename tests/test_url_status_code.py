import requests


def test_url_status_code(url_param, status_code_param):
    response = requests.get(url=url_param)
    assert response.status_code == status_code_param
