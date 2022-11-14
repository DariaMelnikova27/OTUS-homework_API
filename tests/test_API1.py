import pytest
import requests as requests

# Тесты API https://dog.ceo/api/

base_url = 'https://dog.ceo/api/'


# Кейс 1. Проверка, что код ответа 200
def test_get_status_code_equals_200():
    response = requests.get(base_url + 'breeds/list/all')
    assert response.status_code == 200


# Кейс 2. Проверка, что формат ответа json
def test_get_json():
    response = requests.get(base_url + 'breeds/list/all')
    assert response.headers['Content-Type'] == 'application/json'


# Кейс 3. Проверка наличия в полном списке пород различных подвидов гончих (hound)
sub_hound = ['afghan', 'basset', 'blood', 'english', 'ibizan', 'plott', 'walker']


def test_hound_type():
    response = requests.get(base_url + 'breed/hound/list')
    assert response.json()['message'] == sub_hound


# Кейс 4. Проверка, что картинка в формате jpg
@pytest.mark.parametrize('breed', ['beagle', 'chihuahua', 'vizsla'])
def test_image_format_equals_jpg(breed):
    response = requests.get(base_url + 'breed/' + breed + '/images')
    for items in response.json()['message']:
        assert items[-4:] == '.jpg'


# Кейс 5. Проверка наличия или отсутствия подвидов пород
@pytest.mark.parametrize("breed, sub_breed", [("hound", True), ("affenpinscher", False)])
def test_sub_breed(breed, sub_breed):
    response = requests.get(base_url + "breed/" + breed + "/list")
    if sub_breed:
        assert len(response.json()["message"]) > 0
    else:
        assert len(response.json()["message"]) == 0
