import requests

def test_create_post_with_auth():
    url = "https://jsonplaceholder.typicode.com/posts"

    headers = {
        "Authorization": "Bearer fake_token_123",
        "Content-Type": "application/json"
    }

    payload = {
        "title": "Authorization Test",
        "body": "Bu post header ile gönderildi",
        "userId": 99
    }

    response = requests.post(url, json=payload, headers=headers)

    # Status kontrol
    assert response.status_code == 201

    # İçerik kontrol
    response_json = response.json()
    assert response_json["userId"] == payload["userId"]
    assert response_json["title"] == payload["title"]
