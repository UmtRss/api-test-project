import requests

def test_get_post():
    url = "https://jsonplaceholder.typicode.com/posts/1"

    response = requests.get(url)

    # Status kod kontrolü
    assert response.status_code == 200

    # JSON içerik kontrolü
    response_json = response.json()
    assert response_json["id"] == 1
    assert response_json["userId"] == 1
    assert "title" in response_json
    assert "body" in response_json
