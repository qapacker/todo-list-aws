import requests

BASE_URL = "https://v5wqv9mpki.execute-api.us-east-1.amazonaws.com/Prod/todos"
HEADERS = {"Content-Type": "application/json"}

def test_1_list_todos():
    response = requests.get(BASE_URL)
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_2_create_todo():
    payload = {
        "id": "1",
        "task": "Learn AWS SAM",
        "done": True
    }
    response = requests.post(BASE_URL + "/", json=payload, headers=HEADERS)
    assert response.status_code in (200, 201)

def test_3_get_todo():
    response = requests.get(BASE_URL + "/1")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == "1"
    assert "task" in data

def test_4_update_todo():
    payload = {
        "task": "Learn AWS SAM in depth",
        "done": True
    }
    response = requests.put(BASE_URL + "/1", json=payload, headers=HEADERS)
    assert response.status_code == 200

def test_5_delete_todo():
    response = requests.delete(BASE_URL + "/1")
    assert response.status_code == 200
