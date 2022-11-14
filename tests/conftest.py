import pytest


# Фикстуры для тестовой функции, принимающей url и status_code

def pytest_addoption(parser):
    parser.addoption(
        "--url",
        default="https://ya.ru",
        help="This is request url"
    )
    parser.addoption(
        "--status_code",
        default="200",
        help="This is expected request status code",
        type=int
    )


@pytest.fixture
def url_param(request):
    return request.config.getoption("--url")


@pytest.fixture
def status_code_param(request):
    return request.config.getoption("--status_code")
