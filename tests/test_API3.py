import pytest
import requests

# Тесты API https://jsonplaceholder.typicode.com/

base_url = 'https://jsonplaceholder.typicode.com/'


# Кейс 1. Проверка, что список содержит 100 id
def test_id_quantity():
    response = requests.get(base_url + 'posts')
    assert len(response.json()) == 100


# Кейс 2. Проверка существования записей для пользователей с userId == [1, 2, 3]
@pytest.mark.parametrize('user_id', [1, 2, 3])
def test_user_id_1_2_3_exists(user_id):
    response = requests.get(base_url + 'posts?userId=' + str(user_id))
    assert len(response.json()) > 0


# Кейс 3. Проверка корректности работы сортировки по альбомам
@pytest.mark.parametrize('album_id', [4, 7, 10])
def test_filtering_by_album_id(album_id):
    response = requests.get(base_url + "albums/" + str(album_id) + "/photos")
    assert len(response.json()) > 0


# Кейс 4. Проверка возможности обновления ресурса
def test_updating_a_resource():
    response = requests.put(base_url + "posts/1",
                            data={'title': 'qwerty', 'body': '12345', 'userId': 9})
    response_json = response.json()
    assert response_json['title'] == 'qwerty'
    assert response_json['body'] == '12345'
    assert response_json['userId'] == '9'


# Кейс 5. Проверка возможности удаления ресурса
def test_deleting_a_resource():
    response = requests.delete(base_url + "posts/1")
    assert response.status_code == 200
