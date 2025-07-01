import requests
import json

BASE_URL = "https://1jdpqyai5d.execute-api.us-east-1.amazonaws.com/Prod/todos"
HEADERS = {"Content-Type": "application/json"}

todo_id = None

def test_1_list_todos():
    response = requests.get(BASE_URL)
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_2_create_todo():
    global todo_id
    payload = {
        "text": "Learn AWS SAM"
    }
    response = requests.post(BASE_URL + "/", json=payload, headers=HEADERS)
    assert response.status_code in (200, 201)

    # doble json.loads porque tu Lambda devuelve body como string
    outer = response.json()
    inner = json.loads(outer["body"])
    todo_id = inner["id"]
    assert "text" in inner

def test_3_get_todo():
    global todo_id
    assert todo_id is not None
    response = requests.get(BASE_URL + "/" + todo_id)
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == todo_id

def test_4_update_todo():
    global todo_id
    payload = {
        "text": "Learn AWS SAM in depth",
        "checked": True
    }
    response = requests.put(BASE_URL + "/" + todo_id, json=payload, headers=HEADERS)
    assert response.status_code in (200, 204)

def test_5_delete_todo():
    global todo_id
    response = requests.delete(BASE_URL + "/" + todo_id)
    assert response.status_code in (200, 204)
