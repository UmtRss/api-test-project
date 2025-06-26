import requests
import allure


@allure.title("Create a new post via API")
@allure.description("Sends a POST request to create a new post and validates the response content.")
def test_create_post_allure():
    url = "https://jsonplaceholder.typicode.com/posts"

    payload = {
        "title": "Integration Testing",
        "body": "Testing API behavior with proper payload.",
        "userId": 7
    }

    with allure.step("Send POST request to the endpoint"):
        response = requests.post(url, json=payload)

    with allure.step("Verify response status code is 201"):
        assert response.status_code == 201

    with allure.step("Validate response body matches sent data"):
        response_json = response.json()
        assert response_json["title"] == payload["title"]
        assert response_json["body"] == payload["body"]
        assert response_json["userId"] == payload["userId"]
