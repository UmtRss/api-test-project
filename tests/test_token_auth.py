import requests
import allure
import pytest

@pytest.mark.skip(reason="Token-based auth test is for educational purposes. Requires real API key.")
@allure.title("Register and authenticated request using token")
@allure.description("Registers a user and uses token to access protected resource. Currently skipped.")
def test_register_and_get_users():
    register_url = "https://reqres.in/api/register"
    user_url = "https://reqres.in/api/users?page=2"

    register_payload = {
        "email": "eve.holt@reqres.in",
        "password": "pistol"
    }

    with allure.step("Send registration request and get token"):
        response = requests.post(register_url, json=register_payload)
        assert response.status_code == 200
        token = response.json()["token"]

    with allure.step("Use token in Authorization header to access protected endpoint"):
        headers = {
            "Authorization": f"Bearer {token}"
        }
        user_response = requests.get(user_url, headers=headers)
        assert user_response.status_code == 200
        assert "data" in user_response.json()
