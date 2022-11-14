import pytest
import requests

# Тесты API https://api.openbrewerydb.org/breweries

base_url = 'https://api.openbrewerydb.org/breweries'


# Кейс 1. Проверка, что код ответа 404 при невалидной ссылке
def test_get_status_code_equals_404():
    response = requests.get(base_url + 'lalala')
    assert response.status_code == 404


# Кейс 2. Проверка, что json пивоварни 10 Barrel Brewing Co имеет все необходимые ключи
def test_keys():
    keys_default = ['id',
                    'name',
                    'brewery_type',
                    'street',
                    'address_2',
                    'address_3',
                    'city',
                    'state',
                    'county_province',
                    'postal_code',
                    'country',
                    'longitude',
                    'latitude',
                    'phone',
                    'website_url',
                    'updated_at',
                    'created_at']
    list_dict = requests.get(base_url + '/10-barrel-brewing-co-san-diego').json()
    keys_list = list(list_dict.keys())
    assert keys_default == keys_list


# Кейс 3. Проверка различного количества пивоварен на странице
@pytest.mark.parametrize('quantity', [1, 5, 16, 50])
def test_quantity(quantity):
    response = requests.get(base_url + '/random?size=' + str(quantity))
    assert len(response.json()) == quantity


# Кейс 4. Проверка сортировки по штату
@pytest.mark.parametrize('state', ['New York', 'Minnesota', 'Iowa'])
def test_by_state(state):
    response = requests.get(base_url + '?by_state=' + state)
    for items in response.json():
        assert items['state'] == state


# Кейс 5. Проверка, что дефолтное количество пивоварен на странице 20
def test_default_len():
    response = requests.get(base_url + '?per_page=')
    assert len(response.json()) == 20
