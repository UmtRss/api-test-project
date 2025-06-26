import pytest
import requests

@pytest.mark.parametrize("title, body, user_id", [
    ("Test 1", "Body 1", 1),
    ("Test 2", "Body 2", 2),
    ("", "Boş Title", 3),              # Negative Case
    ("Title 4", "", 4),                # Negative Case
])
def test_create_post_parametrize(title, body, user_id):
    url = "https://jsonplaceholder.typicode.com/posts"

    payload = {
        "title": title,
        "body": body,
        "userId": user_id
    }

    response = requests.post(url, json=payload)

    # Status code kontrolü
    assert response.status_code == 201

    # Response body kontrolü
    response_json = response.json()
    assert response_json["title"] == title
    assert response_json["body"] == body
    assert response_json["userId"] == user_id
