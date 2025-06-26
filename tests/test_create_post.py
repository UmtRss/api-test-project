import requests

def test_create_post():
    url = "https://jsonplaceholder.typicode.com/posts"

    payload = {
        "title": "Kanka Test",
        "body": "Bu API testidir",
        "userId": 42
    }

    response = requests.post(url, json=payload)

    # Status kodu kontrol et
    assert response.status_code == 201

    # İçeriği kontrol et
    response_json = response.json()
    assert response_json["title"] == payload["title"]
    assert response_json["body"] == payload["body"]
    assert response_json["userId"] == payload["userId"]
